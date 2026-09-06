# clash-proxy-issue

## clash-proxy-7897-issue

- 这里通常会有一个问题，导致在启动/部署 `公网/localhost暴露服务` 时发生异常。

- 这是由于 clash 开启了 `clash tun/system proxy` ，而终端的代理环境变量设置与 python 不兼容。具体见 Q1 。

- 只需设置一下环境代理参数即可：

    ```bash
    export ALL_PROXY="http://127.0.0.1:7897"
    export all_proxy="http://127.0.0.1:7897"
    ./ebook2audiobook.command
    ```

- QA
  - Q1:为什么在 Clash 里开了 System Proxy 和 TUN，`其他软件都正常，而这里会报错`？
  - A1:`环境变量优先级高于 TUN 虚拟网卡`。
    - 普通图形软件 / 浏览器：没有读取 Linux 终端的环境变量，它们发出的所有网络流量都是直接从操作系统网络协议栈走，被 Clash 的 TUN 虚拟网卡 透明捕获并转发，因此完全正常。  
    - Python 程序：Python 的网络库（包括 requests、httpx、urllib 等）有自己的规则：只要当前环境存在 ALL_PROXY 或 HTTP_PROXY 环境变量，它们就会优先使用环境变量指定的代理服务器进行应用层转发，而不会直接去走系统的默认网关/TUN 虚拟网卡。
  - Q2:为什么`环境变量会导致报错`？
  - A2:因为默认给终端设置的环境变量 python `默认不支持`
    - 默认设置的环境变量是这样的

        ```bash
        HTTP_PROXY=http://127.0.0.1:7897
        HTTPS_PROXY=http://127.0.0.1:7897
        ALL_PROXY=socks://127.0.0.1:7897
        ```

    - 但是 python `默认不认 socks` 只认 socks5。`要么装兼容库，要么改掉环境变量`。

## clash-proxy-routing-issue

- 这里通常会有一个问题，导致 `中国大陆以外的流量` 错误地走代理，反而连不上了。

- 转发规则有问题。

- clash 覆写脚本里添加规则即可（可能有更好的做法）

## clash-proxy-fakeip-reset-network-issue

未解决。
