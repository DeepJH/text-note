# Android 开发入门流程

> 适合第一次做 Android 开发的人阅读。本文按真实项目流程组织：先搭环境，再写一个能运行的最小版本，然后逐步补功能、测试、调试、打包和发布。

## 1. 先理解 Android 开发在做什么

Android App 本质上由几部分组成：

- **界面 UI**：用户看到和点击的内容。新项目优先使用 Kotlin + Jetpack Compose + Material 3。
- **状态 State**：界面当前显示的数据，例如是否登录、设备列表、订单状态、加载中、错误信息。
- **业务逻辑**：例如登录、扫描蓝牙设备、创建订单、结束订单。
- **数据层**：网络请求、本地数据库、缓存、系统能力调用（蓝牙、定位、通知等）。
- **系统配置**：权限、App 名称、图标、最低系统版本、签名、混淆规则等。

推荐的心智模型是：**界面只负责展示和触发事件，业务逻辑放到 ViewModel/UseCase/Repository，系统能力和网络请求放到数据层**。不要把所有代码都写进一个 Activity。

## 2. 推荐技术栈

新手不建议一开始同时学太多旧方案。推荐从这套开始：

- **语言**：Kotlin
- **IDE**：Android Studio 最新稳定版
- **UI**：Jetpack Compose
- **设计组件**：Material 3
- **架构**：单 Activity + Compose Navigation + ViewModel + Repository
- **异步**：Kotlin Coroutines + Flow
- **网络**：Retrofit 或 Ktor Client
- **JSON**：kotlinx.serialization 或 Moshi
- **本地存储**：DataStore（简单键值）/ Room（结构化数据库）
- **依赖注入**：小项目可先手写依赖；复杂后再引入 Hilt
- **测试**：JUnit、MockK、Compose UI Test、Android Instrumented Test

不推荐新手一开始选择：

- Java + XML + 多 Activity 的传统写法，除非维护老项目。
- 一上来就做大而全的框架封装。
- 直接复制网上一大段权限、蓝牙、网络代码但不理解生命周期和异常处理。

## 3. 环境搭建

### 3.1 安装工具

1. 安装 Android Studio。
2. 第一次打开后按向导安装 Android SDK、Platform Tools、Emulator。
3. 创建一个 Android Virtual Device（AVD）模拟器。
4. 准备一台真机，打开开发者选项和 USB 调试。

建议同时具备：

- **模拟器**：适合快速验证不同屏幕、系统版本、横竖屏。
- **真机**：必须用于蓝牙、传感器、相机、系统权限、后台行为等场景。

### 3.2 检查项目能否构建

新建项目后，在项目根目录运行：

```bash
./gradlew assembleDebug
```

常用命令：

```bash
./gradlew test
./gradlew connectedAndroidTest
./gradlew lint
./gradlew assembleDebug
./gradlew bundleRelease
```

含义：

- `test`：运行本地单元测试。
- `connectedAndroidTest`：在连接的真机或模拟器上运行测试。
- `lint`：检查潜在问题，例如权限、兼容性、资源、性能。
- `assembleDebug`：构建调试 APK。
- `bundleRelease`：构建发布用 Android App Bundle。

## 4. 新建项目时怎么选

Android Studio 新建项目时建议选择：

- Template：`Empty Activity`
- Language：`Kotlin`
- UI：`Jetpack Compose`
- Minimum SDK：根据目标用户决定。新手项目可先选一个覆盖面较大的版本，不要盲目选太高。
- Package name：使用反向域名格式，例如 `com.example.qzxyclient`。正式项目不要用 `example`。

创建后先不要急着写功能，先运行默认 App：

1. 点 Run。
2. 确认模拟器或真机能安装并启动。
3. 改一行页面文字，再运行一次。
4. 确认你知道“改代码 -> 构建 -> 安装 -> 运行”的循环。

## 5. 项目结构怎么看

典型 Android 项目结构：

```text
project/
  settings.gradle.kts
  build.gradle.kts
  gradle.properties
  app/
    build.gradle.kts
    src/
      main/
        AndroidManifest.xml
        java/ 或 kotlin/
        res/
      test/
      androidTest/
```

重点文件：

- `settings.gradle.kts`：声明项目包含哪些模块。
- 根目录 `build.gradle.kts`：配置插件版本、仓库等全局构建信息。
- `app/build.gradle.kts`：配置 App 模块，例如 SDK 版本、依赖、构建类型。
- `AndroidManifest.xml`：声明权限、Activity、Service、Provider 等。
- `src/main/kotlin`：主代码。
- `src/main/res`：图标、字符串、颜色、资源。
- `src/test`：本地 JVM 测试。
- `src/androidTest`：需要 Android 设备或模拟器的测试。

## 6. 写代码的基本流程

实际开发不要先写一堆页面，推荐按“纵向切片”做功能。每次只做一条能跑通的小流程。

### 6.1 一个功能的开发顺序

例如做“登录”：

1. 定义页面状态：手机号、密码、加载中、错误提示、是否登录成功。
2. 写 Compose 页面：输入框、按钮、错误提示。
3. 写 ViewModel：接收用户事件，调用登录逻辑，更新状态。
4. 写 Repository：负责真正请求接口。
5. 写数据模型：请求参数、响应数据、错误结构。
6. 写测试：验证密码校验、登录成功、登录失败、网络异常。
7. 真机运行：手动验证输入、加载状态、错误提示、旋转屏幕后状态是否合理。

### 6.2 推荐目录组织

小项目可以这样分：

```text
app/src/main/kotlin/com/your/package/
  MainActivity.kt
  app/
    AppNavHost.kt
  feature/
    login/
      LoginScreen.kt
      LoginViewModel.kt
      LoginUiState.kt
    home/
      HomeScreen.kt
      HomeViewModel.kt
  data/
    network/
      ApiService.kt
      NetworkClient.kt
    repository/
      AuthRepository.kt
      DeviceRepository.kt
  model/
    User.kt
    Device.kt
    Order.kt
  core/
    Result.kt
    ErrorMapper.kt
```

复杂后可以拆模块，但新手阶段先保持一个 `app` 模块即可。

## 7. Compose 界面怎么写

Compose 是声明式 UI：你描述“当前状态下界面应该长什么样”，状态变了，界面自动重组。

基本模式：

```kotlin
data class LoginUiState(
    val phone: String = "",
    val password: String = "",
    val loading: Boolean = false,
    val error: String? = null
)
```

```kotlin
@Composable
fun LoginScreen(
    state: LoginUiState,
    onPhoneChange: (String) -> Unit,
    onPasswordChange: (String) -> Unit,
    onLoginClick: () -> Unit
) {
    // TextField、Button、Text 等 UI 组件放这里
}
```

原则：

- Composable 尽量是“无状态”的：状态从外部传入，事件回调给外部。
- 不要在 Composable 里直接发网络请求。
- 列表使用 `LazyColumn`，不要用普通 `Column` 渲染大量数据。
- 文案放到 `strings.xml`，不要到处硬编码字符串。
- 颜色、间距、字体尽量走 Material Theme，不要每个页面随手写一套。
- 适配深色模式、横竖屏、不同字体大小。

## 8. 状态和 ViewModel

ViewModel 负责：

- 保存 UI 状态。
- 接收用户事件。
- 调用业务逻辑或 Repository。
- 处理加载、成功、失败。

不要让 ViewModel：

- 持有 Activity、View、Context 的长生命周期引用。
- 直接操作界面控件。
- 直接拼接复杂 HTTP 请求细节，网络细节应放到 Repository 或 API 层。

常见状态建议统一表达：

```kotlin
sealed interface LoadState<out T> {
    data object Idle : LoadState<Nothing>
    data object Loading : LoadState<Nothing>
    data class Success<T>(val data: T) : LoadState<T>
    data class Error(val message: String, val cause: Throwable? = null) : LoadState<Nothing>
}
```

这样页面可以清楚地区分空闲、加载中、成功和失败。

## 9. 网络请求注意事项

网络层重点不是“能请求成功”，而是要能处理异常：

- 无网络。
- 超时。
- 服务端返回错误码。
- JSON 字段缺失或类型变化。
- Token 过期。
- 重复点击导致重复请求。
- 页面离开后请求仍在执行。

规范建议：

- 所有接口定义集中管理。
- 请求和响应模型单独定义。
- 不在 UI 层拼 URL。
- 不在日志里打印密码、Token、手机号、身份证等敏感数据。
- 对错误做统一转换，给用户显示可理解的提示。
- 调试环境和正式环境分开配置。
- HTTPS 优先，不要为了省事全局允许明文 HTTP。

## 10. 权限和系统能力

Android 权限分为安装时声明和运行时申请。新手最常见错误是：只在 `AndroidManifest.xml` 写了权限，但没有在运行时向用户申请。

常见权限场景：

- 网络：`INTERNET`，只需 manifest 声明。
- 蓝牙扫描/连接：Android 12 及以上需要 `BLUETOOTH_SCAN`、`BLUETOOTH_CONNECT` 等运行时权限。
- 旧系统蓝牙扫描可能涉及定位权限。
- 后台定位、后台蓝牙扫描、前台服务都有更严格限制。
- 通知权限在新系统上也需要运行时申请。

权限处理原则：

- 只申请当前功能确实需要的权限。
- 用户拒绝权限时要有降级体验或清晰提示。
- 不要在首次启动时一次性申请所有权限。
- 不要通过误导性文案诱导用户授权。
- 涉及蓝牙、定位、账号、支付、订单的功能，要特别注意隐私和合规。

如果项目涉及校园设备、蓝牙设备、下单或支付，一定要确认你有合法授权。不要绕过服务条款、访问控制、计费逻辑或设备安全机制。

## 11. 本地存储怎么选

按用途选择：

- **DataStore**：保存登录状态、用户设置、简单 Token。
- **Room**：保存结构化列表、缓存数据、离线数据。
- **文件存储**：保存图片、日志、导出文件。
- **EncryptedSharedPreferences / 加密方案**：保存敏感数据时考虑使用。

不要做：

- 把密码明文存在本地。
- 把 Token 打到日志。
- 把接口密钥硬编码到客户端后以为安全。
- 把大量业务数据塞进 SharedPreferences。

## 12. 测试怎么做

测试分几层，不要只靠手点。

### 12.1 本地单元测试

位置：`src/test`

适合测试：

- 普通 Kotlin 函数。
- 数据转换。
- 参数校验。
- Repository 中可替换依赖的逻辑。
- ViewModel 状态变化。

命令：

```bash
./gradlew test
```

### 12.2 设备测试

位置：`src/androidTest`

适合测试：

- Compose UI 交互。
- 需要 Android Framework 的能力。
- Room 数据库。
- 权限相关流程。

命令：

```bash
./gradlew connectedAndroidTest
```

### 12.3 手动测试清单

每个功能至少手动测这些：

- 首次安装。
- 升级安装。
- 无网络。
- 弱网或超时。
- 权限拒绝。
- 权限授权后再进入。
- 横竖屏切换。
- 深色模式。
- 字体放大。
- App 切后台再回来。
- 杀进程后重新打开。
- 快速重复点击按钮。
- 服务端返回异常数据。

蓝牙类功能还要测：

- 蓝牙关闭。
- 无权限。
- 附近没有设备。
- 多个设备同时出现。
- 设备连接失败。
- 扫描中离开页面。
- 不同 Android 版本的权限差异。
- 不同厂商手机的后台限制。

## 13. 调试技巧

常用工具：

- **Logcat**：看日志和崩溃堆栈。
- **Debugger**：断点调试。
- **Layout Inspector**：检查界面层级。
- **Network Inspector**：检查网络请求。
- **Profiler**：看 CPU、内存、耗电。
- **App Inspection**：查看数据库等运行时数据。

日志建议：

- 给日志统一 tag。
- Debug 包可以多打日志，Release 包要减少日志。
- 不输出密码、Token、手机号、定位、设备唯一标识等敏感信息。
- 崩溃日志要保留完整堆栈，先看第一处 `Caused by`。

调试思路：

1. 先复现问题。
2. 看崩溃堆栈或错误日志。
3. 缩小范围：UI、状态、网络、本地存储、权限、系统能力。
4. 加最少量日志验证假设。
5. 修复后补测试或手动回归清单。

## 14. Git 和开发流程

建议从第一天就用 Git：

```bash
git status
git add .
git commit -m "Add login screen"
```

基本习惯：

- 每次提交只做一件事。
- 提交信息写清楚做了什么。
- 不提交 `local.properties`、签名文件、密钥、临时日志。
- 新功能开分支，完成后合并。
- 遇到大改动先提交一个稳定点。

推荐 `.gitignore` 至少覆盖：

- `.gradle/`
- `build/`
- `local.properties`
- `.idea/` 中与个人环境强相关的文件
- 签名 keystore
- 临时日志和导出文件

## 15. 代码规范

### 15.1 命名

- 类名：`LoginViewModel`、`DeviceRepository`
- 函数名：`login()`、`scanDevices()`
- 状态类：`LoginUiState`
- 事件：`onLoginClick()`、`onDeviceSelected()`
- Composable：首字母大写，例如 `LoginScreen`

### 15.2 Kotlin 习惯

- 优先使用不可变数据：`val` 优先于 `var`。
- 用 `data class` 表达数据。
- 用 `sealed interface` 表达有限状态。
- 避免到处使用可空类型，必要时尽早处理。
- 避免空捕获异常：不要 `catch (e: Exception) {}` 什么都不做。
- 协程里注意取消和生命周期。

### 15.3 UI 规范

- 保持 Material 3 风格一致。
- 按钮、输入框、列表、弹窗使用系统或 Material 组件。
- 所有可点击元素要有明确反馈。
- 加载中要禁用重复提交。
- 错误提示要能被用户理解。
- 重要操作要二次确认，例如结束订单、退出登录。
- 适配深色模式和大字体。
- 不要把文字写死在图片里。

### 15.4 架构规范

- UI 层不直接访问网络。
- Repository 不直接控制 UI。
- 数据模型和 UI 状态分开。
- 一个类只做一类事情。
- 权限请求和业务动作分开处理。
- 长耗时任务不要阻塞主线程。

## 16. 性能和稳定性注意事项

常见坑：

- 在主线程做网络、数据库、大量计算。
- 列表一次性渲染太多元素。
- 图片未压缩导致内存暴涨。
- 协程作用域用错导致页面退出后任务还在跑。
- 蓝牙扫描没有及时停止。
- 轮询太频繁导致耗电。
- Activity 重建后状态丢失。
- 重复点击创建多个订单或请求。

改进方式：

- 网络和数据库放到 IO 线程。
- 大列表使用懒加载。
- 图片使用合适尺寸。
- 使用 ViewModel 保存页面状态。
- 页面离开时停止扫描、取消监听。
- 对按钮做 loading 和防重复提交。
- 对关键接口做幂等或客户端保护。

## 17. 打包和发布

发布前要确认：

- `applicationId` 正式且不可随意更改。
- `versionCode` 每次发布递增。
- `versionName` 给用户看，语义清晰。
- Release 包使用正式签名。
- 开启必要的 R8/混淆，并保留反序列化、反射相关规则。
- Debug 地址、测试账号、测试日志不要进 Release 包。
- 隐私政策、权限说明、第三方 SDK 合规材料准备好。
- 用内部测试渠道先发给少量用户验证。

构建发布包：

```bash
./gradlew bundleRelease
```

Google Play 通常使用 Android App Bundle（`.aab`）。如果是企业内部分发或本地安装，也可能需要 APK。

## 18. 新手建议的学习路线

### 第 1 阶段：能跑起来

- 安装 Android Studio。
- 新建 Empty Activity。
- 理解 `MainActivity`、Composable、Gradle、Manifest。
- 改页面文字、按钮点击、输入框。

### 第 2 阶段：做一个小功能

- 做登录页或待办列表。
- 学会 UI 状态。
- 学会 ViewModel。
- 学会本地单元测试。

### 第 3 阶段：接入真实能力

- 接网络请求。
- 处理 loading/error/success。
- 保存登录状态。
- 加导航。

### 第 4 阶段：做完整闭环

- 权限申请。
- 真机测试。
- 崩溃处理。
- 打 Release 包。
- 写 README 和测试清单。

## 19. 每次开发前的检查清单

开始写代码前问自己：

- 这个功能的输入是什么？
- 输出是什么？
- 失败情况有哪些？
- 需要哪些权限？
- 是否涉及隐私或敏感数据？
- UI 状态有哪些？
- 是否需要本地缓存？
- 是否需要防重复点击？
- 怎么测试？

提交前检查：

- App 能启动。
- 相关功能手动跑过。
- `./gradlew test` 通过。
- `./gradlew lint` 没有必须修复的问题。
- 没有提交密钥、Token、账号密码。
- 没有无意义大文件。
- 错误提示和边界状态处理过。

## 20. 项目相关的额外提醒

如果你的目标是开发一个带登录、蓝牙扫描、设备选择、下单、结束订单的客户端，建议按这个顺序做：

1. 先做静态 UI：登录页、首页设备分类、订单参数页、订单状态页。
2. 再做假数据流程：不用真实接口，先让页面跳转和状态变化跑通。
3. 接登录接口：处理成功、失败、过期。
4. 接设备列表或蓝牙扫描：先在真机上验证权限和扫描生命周期。
5. 接订单参数：校验输入范围，不允许无效订单。
6. 接下单和结束订单：加 loading、防重复点击、失败重试和二次确认。
7. 做完整回归：登录 -> 扫描 -> 选择设备 -> 下单 -> 结束订单 -> 退出。

对蓝牙和订单类功能要格外谨慎：

- 扫描必须有明确开始和停止时机。
- App 进后台时要考虑是否继续扫描，继续扫描可能需要前台服务和通知。
- 下单、结束订单这类操作不能只靠前端按钮状态保护，服务端也应有校验。
- 不要绕过官方授权、计费或设备安全机制。

## 21. 推荐官方资料

- Android Studio 安装文档：<https://developer.android.com/studio/install>
- Jetpack Compose：<https://developer.android.com/compose>
- Android App Architecture：<https://developer.android.com/topic/architecture>
- Android 构建配置：<https://developer.android.com/build>
- Android 测试基础：<https://developer.android.com/training/testing/fundamentals>
- Android App Quality：<https://developer.android.com/quality>
- Android 蓝牙权限：<https://developer.android.com/guide/topics/connectivity/bluetooth/permissions>

## 22. 一句话总结

Android 开发不是只写页面，而是持续处理“状态、权限、生命周期、异常、兼容性和测试”。新手最稳的做法是：先做最小可运行版本，再按一个个小功能纵向打通，每个功能都补上错误处理和测试清单。
