# JavaScript 语法快速入门

> 面向有 Python/C 基础的开发者

---

## 1. 变量声明

JavaScript 有三种声明变量的方式，类似于 C 的作用域概念：

```javascript
let age = 25;           // 块级作用域，可重新赋值
const name = "Alice";   // 块级作用域，不能重新赋值
var score = 100;        // 函数作用域（旧语法，Avoid）

// 对比 Python:
// age = 25              # Python 中无 let/const
// AGE = 25              # Python 约定大写为常量
```

**关键区别**：
- `let` 和 `const` 是 ES6 引入的块级作用域（像 C 的大括号块）
- `var` 是旧语法，作用域是函数级别（容易产生 bug）

---

## 2. 基本数据类型

JavaScript 是动态类型语言，但有类型概念（像 Python）：

```javascript
// 原始类型
let num = 42;           // Number（类似 Python int/float 不分）
let str = "Hello";      // String
let bool = true;        // Boolean
let empty = null;       // 空值（明确赋值为空）
let notDefined;         // undefined（未初始化）
let sym = Symbol("id"); // 唯一标识符
let big = 123n;         // BigInt（大整数）

// 对比 Python 类型:
// int    → Number
// float  → Number  
// str    → String
// bool   → Boolean
// None   → null / undefined
```

**检查类型**：

```javascript
typeof 42        // "number"
typeof "hello"  // "string"
typeof true     // "boolean"
typeof null     // "object" （历史 bug，注意！）
```

---

## 3. 运算符

### 算术运算符（与 C/Python 相同）
```javascript
+, -, *, /, %, **  // ** 是幂运算符（Python 用 **，C 没有）
```

### 比较运算符
```javascript
// == 会转换类型比较（类似 Python 自动转换）
// === 严格比较（推荐）
"5" == 5    // true  （类型转换）
"5" === 5   // false （严格比较）

// Python: == 会比较值，但 "5" == 5 在 Python 中也是 True
// C:       == 比较指针/值，"5" == 5 需要手动转换
```

### 逻辑运算符
```javascript
&&, ||, !        // 与 C 相同（Python 用 and, or, not）
```

### 空值合并运算符（ES6）
```javascript
let x = null ?? "default";  // "default"（null/undefined 时取值）
```

---

## 4. 字符串

```javascript
// 普通字符串
let s1 = "Hello";
let s2 = 'World';

// 模板字符串（类似 Python f-string）
let name = "Alice";
let msg = `Hello, ${name}!`;  // "Hello, Alice!"

// 多行字符串
let multi = `
  第一行
  第二行
`;

// 常用方法（类似 Python str 方法）
"hello".toUpperCase()  // "HELLO"
"hello".length         // 5
"hello".includes("ell")// true
"hello".slice(1, 4)   // "ell"
```

---

## 5. 数组

类似 Python list，但更灵活：

```javascript
let arr = [1, 2, 3, "four", true];

// 访问（与 Python 相同）
arr[0]      // 1
arr.length  // 5

// 常用方法
arr.push(6);       // 末尾添加，返回新长度
arr.pop();         // 末尾删除，返回删除元素
arr.map(x => x * 2)     // [2, 4, 6, 8, 10, 12] - 类似 Python list comprehension
arr.filter(x => x > 2)  // [3, 4, 5, 6]
arr.reduce((sum, x) => sum + x, 0)  // 21 - 类似 Python reduce

// 展开操作符（ES6）
let newArr = [...arr, 7, 8];  // 合并数组

// 对比 Python:
// arr.append()  → arr.push()
// list comprehension → arr.map()
// [x for x in lst if x > 2] → arr.filter(x => x > 2)
```

---

## 6. 对象

类似 Python dict，但语法不同：

```javascript
// 创建对象
let person = {
  name: "Alice",
  age: 25,
  greet: function() { return "Hello!"; }  // 方法
};

// 访问属性（两种方式）
person.name     // "Alice"
person["name"]  // "Alice"

// ES6 简写
let name = "Alice";
let age = 25;
let p = { name, age };  // { name: "Alice", age: 25 }

// 解构赋值（ES6）
let { name, age } = person;  // 提取属性
let { name: n } = person;    // 重命名

// 对比 Python:
// d = {"name": "Alice", "age": 25}
// d["name"] 或 d.get("name")
```

---

## 7. 控制流

### 条件语句

```javascript
// if-else（与 C 相同）
if (x > 10) {
  console.log("big");
} else if (x > 5) {
  console.log("medium");
} else {
  console.log("small");
}

// 三元运算符（类似 C）
let label = x > 5 ? "big" : "small";

// switch（与 C 相同）
switch (day) {
  case 0: console.log("Sun"); break;
  case 1: console.log("Mon"); break;
  default: console.log("Other");
}
```

### 循环

```javascript
// for 循环（与 C 相同）
for (let i = 0; i < 5; i++) {
  console.log(i);
}

// for...of（类似 Python for x in list）
for (let item of arr) {
  console.log(item);
}

// for...in（遍历对象键，类似 Python dict 遍历）
for (let key in person) {
  console.log(key, person[key]);
}

// forEach
arr.forEach((item, index) => console.log(index, item));

// while（与 C 相同）
while (condition) { }

// 对比 Python:
// for x in lst:      → for (let x of arr)
// for i, x in enumerate(lst):  → arr.forEach((x, i) => {})
```

---

## 8. 函数

JavaScript 函数是一等公民，非常灵活：

### 函数声明

```javascript
// 传统函数（类似 C）
function add(a, b) {
  return a + b;
}

// 函数表达式
const multiply = function(a, b) {
  return a * b;
};

// 箭头函数（ES6，重要！）
const divide = (a, b) => a / b;           // 单行返回
const greet = name => `Hello, ${name}!`;  // 单参数可省略括号
const log = () => console.log("Log");    // 无参数需要括号

// 对比 Python:
// def add(a, b): return a + b
// lambda a, b: a + b
```

### 参数处理

```javascript
// 默认参数（类似 Python）
function greet(name = "World") {
  return `Hello, ${name}!`;
}

// 剩余参数
function sum(...numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}
sum(1, 2, 3, 4)  // 10

// 解构参数
function printInfo({ name, age }) {
  console.log(name, age);
}
printInfo({ name: "Alice", age: 25 });
```

### 特殊性质

```javascript
// 函数是对象，可以有属性
function foo() {}
foo.custom = "value";

// 函数可以作为参数和返回值
function operation(fn, x, y) {
  return fn(x, y);
}
operation((a, b) => a + b, 3, 4);  // 7
```

---

## 9. 类（ES6）

类似 Python class 语法，但基于原型：

```javascript
class Person {
  constructor(name, age) {
    this.name = name;    // 类似 Python self.name
    this.age = age;
  }

  // 方法（不需要 def，不需要 self）
  greet() {
    return `Hi, I'm ${this.name}`;
  }

  // 静态方法（类似 Python @staticmethod）
  static create(name) {
    return new Person(name, 0);
  }

  // Getter/Setter
  get info() {
    return `${this.name}, ${this.age}`;
  }
}

let p = new Person("Alice", 25);
p.greet();       // "Hi, I'm Alice"
Person.create("Bob");

// 继承（类似 Python super()）
class Student extends Person {
  constructor(name, age, grade) {
    super(name, age);  // 调用父类构造函数
    this.grade = grade;
  }

  greet() {
    return super.greet() + ` I'm in grade ${this.grade}`;
  }
}
```

---

## 10. 模块化

### 导出（export）

```javascript
// 命名导出
export const PI = 3.14;
export function add(a, b) { return a + b; }

// 默认导出
export default class App { }
```

### 导入（import）

```javascript
// 命名导入
import { add, PI } from "./math.js";

// 默认导入
import App from "./App.js";

// 全部导入
import * as utils from "./utils.js";

// 重命名
import { add as sum } from "./math.js";
```

---

## 11. 常用语法糖（ES6+）

### 解构赋值

```javascript
// 数组解构
let [a, b, c] = [1, 2, 3];
let [first, ...rest] = [1, 2, 3, 4];  // rest = [2, 3, 4]

// 对象解构
let { name, age } = { name: "Alice", age: 25 };
let { name: n } = { name: "Alice" };  // n = "Alice"

// 函数参数解构
function f({ x, y }) { return x + y; }
f({ x: 1, y: 2 });  // 3
```

### 展开运算符

```javascript
// 数组展开
let a = [1, 2];
let b = [...a, 3, 4];  // [1, 2, 3, 4]

// 对象展开
let obj = { a: 1, b: 2 };
let obj2 = { ...obj, c: 3 };  // { a: 1, b: 2, c: 3 }

// 函数参数展开
Math.max(...[1, 2, 3]);  // 3
```

### 可选链和空值合并

```javascript
// 可选链（安全访问嵌套属性）
let user = { profile: { name: "Alice" } };
user?.profile?.name;     // "Alice"
user?.address?.city;     // undefined（不报错）

// 空值合并
let x = null ?? "default";  // "default"
let y = 0 ?? "default";      // 0（只对 null/undefined 生效）
```

---

## 12. 异步编程

### Promise

```javascript
// 创建 Promise
const promise = new Promise((resolve, reject) => {
  setTimeout(() => resolve("Done!"), 1000);
});

// 使用
promise
  .then(result => console.log(result))
  .catch(error => console.error(error));

// async/await（类似 Python）
async function fetchData() {
  try {
    const result = await promise;
    console.log(result);
  } catch (e) {
    console.error(e);
  }
}
```

---

## 13. 快速对比表

| 特性 | Python | C | JavaScript |
|------|--------|---|------------|
| 变量声明 | `x = 1` | `int x = 1;` | `let x = 1;` |
| 常量 | 无内置 | `const int X = 1;` | `const X = 1;` |
| 字符串 | `f"Hello {x}"` | `printf("Hello %s", x)` | `` `Hello ${x}` `` |
| 列表/数组 | `[1, 2, 3]` | `int arr[] = {1,2,3};` | `[1, 2, 3]` |
| 字典/对象 | `{"a": 1}` | struct | `{ a: 1 }` |
| 循环 | `for x in lst:` | `for (int i=0; i<n; i++)` | `for (let x of arr)` |
| 函数 | `def foo():` | `void foo() {}` | `function foo() {}` |
| 箭头函数 | lambda x: x*2 | (无直接对应) | `x => x * 2` |
| 类 | `class Foo:` | `struct Foo {};` | `class Foo {}` |
| 类型检查 | 动态 | 静态 | 动态（可加 TS）|

---

## 14. 必知区别

### Python → JavaScript
1. **缩进**：Python 用缩进表示代码块，JavaScript 用大括号 `{}`
2. **打印**：`print(x)` → `console.log(x)`
3. **None**：`None` → `null` 或 `undefined`
4. **列表推导式**：`[x*2 for x in lst]` → `lst.map(x => x * 2)`
5. **类**：`def __init__(self):` → `constructor() {}`

### C → JavaScript
1. **分号**：C 强制分号，JavaScript 可省略（但不建议）
2. **类型**：C 静态类型，JavaScript 动态类型
3. **编译**：C 需编译，JavaScript 解释执行
4. **内存**：C 手动管理，JavaScript 自动垃圾回收

---

## 15. 建议

1. **始终使用 `const` 和 `let`，避免 `var`**
2. **使用 `===` 而不是 `==`**
3. **使用模板字符串而不是字符串拼接**
4. **优先使用箭头函数，但注意 `this` 绑定**
5. **学习 ES6+ 语法，现代 JS 大量使用这些特性**

---

> 建议配合 MDN Web Docs（https://developer.mozilla.org）深入学习。