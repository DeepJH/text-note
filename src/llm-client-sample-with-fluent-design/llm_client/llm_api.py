"""LLM API interface for chat completions."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import AsyncGenerator


@dataclass
class Message:
    """Represents a chat message."""

    role: str  # "user", "assistant", or "system"
    content: str


@dataclass
class LLMConfig:
    """Configuration for LLM API."""

    api_key: str = ""
    base_url: str = "https://api.openai.com/v1"
    model: str = "gpt-3.5-turbo"
    temperature: float = 0.7
    max_tokens: int = 1024


class LLMClient(ABC):
    """Abstract base class for LLM clients."""

    @abstractmethod
    async def chat(
        self,
        messages: list[Message],
        stream: bool = False,
    ) -> str | AsyncGenerator[str, None]:
        """Send a chat completion request to the LLM.

        Args:
            messages: List of messages in the conversation.
            stream: Whether to stream the response.

        Returns:
            If stream=False, the complete response string.
            If stream=True, an async generator yielding response chunks.
        """
        ...


class MockLLMClient(LLMClient):
    """Mock LLM client that returns fixed responses.

    This is a placeholder for development and testing.
    Replace with a real LLM API client when ready.
    """

    FIXED_RESPONSES = {
        "hello": "Hello! How can I assist you today?",
        "help": "I'm here to help! You can ask me questions about various topics.",
        "who are you": "I'm a mock LLM client. I'm a placeholder for a real LLM API integration.",
        "what can you do": "I can demonstrate basic chat functionality. In the future, I'll be connected to a real LLM API to provide intelligent responses.",
    }

    async def chat(
        self,
        messages: list[Message],
        stream: bool = False,
    ) -> str | AsyncGenerator[str, None]:
        """Return a fixed response based on user input."""
        user_message = ""
        for msg in reversed(messages):
            if msg.role == "user":
                user_message = msg.content.lower()
                break

        # Find a matching fixed response
        response = "This is a mock response. The LLM API integration is not yet configured."
        for key, value in self.FIXED_RESPONSES.items():
            if key in user_message:
                response = value
                break

        if stream:
            return self._stream_response(response)
        return response

    async def _stream_response(
        self,
        text: str,
    ) -> AsyncGenerator[str, None]:
        """Simulate streaming by yielding words one at a time."""
        import asyncio

        words = text.split()
        for word in words:
            yield word + " "
            await asyncio.sleep(0.05)


class OpenAIClient(LLMClient):
    """Real LLM client using OpenAI-compatible API.

    This client is ready for integration with any OpenAI-compatible API,
    including OpenAI, Azure OpenAI, local models via Ollama, etc.
    """

    def __init__(self, config: LLMConfig) -> None:
        """Initialize the OpenAI client.

        Args:
            config: LLM configuration with API key and endpoint.
        """
        self.config = config
        self._client = None

    def _get_client(self):
        """Lazy initialization of HTTP client."""
        if self._client is None:
            import httpx

            self._client = httpx.AsyncClient(
                base_url=self.config.base_url,
                headers={
                    "Authorization": f"Bearer {self.config.api_key}",
                    "Content-Type": "application/json",
                },
                timeout=60.0,
            )
        return self._client

    async def chat(
        self,
        messages: list[Message],
        stream: bool = False,
    ) -> str | AsyncGenerator[str, None]:
        """Send a chat completion request to the OpenAI-compatible API."""
        client = self._get_client()

        payload = {
            "model": self.config.model,
            "messages": [
                {"role": msg.role, "content": msg.content} for msg in messages
            ],
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_tokens,
            "stream": stream,
        }

        if stream:
            return self._stream_completion(client, payload)
        else:
            response = await client.post("/chat/completions", json=payload)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]

    async def _stream_completion(
        self,
        client,
        payload: dict,
    ) -> AsyncGenerator[str, None]:
        """Stream chat completion from the API."""
        import json

        async with client.stream("POST", "/chat/completions", json=payload) as response:
            response.raise_for_status()
            async for line in response.aiter_lines():
                if line.startswith("data: "):
                    data = line[6:]
                    if data == "[DONE]":
                        break
                    try:
                        chunk = json.loads(data)
                        delta = chunk.get("choices", [{}])[0].get("delta", {})
                        content = delta.get("content", "")
                        if content:
                            yield content
                    except json.JSONDecodeError:
                        continue


def create_llm_client(config: LLMConfig | None = None) -> LLMClient:
    """Factory function to create an LLM client.

    Args:
        config: Optional LLM configuration. If None or no API key is provided,
                returns a MockLLMClient.

    Returns:
        An LLMClient instance (either MockLLMClient or OpenAIClient).
    """
    if config and config.api_key:
        return OpenAIClient(config)
    return MockLLMClient()
