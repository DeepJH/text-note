# Linux 目录结构简明指南

Linux 的目录结构从 `/`（root directory，根目录）开始，所有文件、程序、配置、设备和挂载点都位于这棵目录树下面。理解常见目录的用途，可以帮助你更快判断文件应该放在哪里、配置应该去哪里找、日志应该从哪里查。

## `/`（root directory，根目录）

`/` 是整个文件系统的起点。绝对路径都从 `/` 开始，例如：

```text
/home/alice/project
/etc/hosts
/var/log/syslog
```

不要把普通文件随意放在 `/` 下。个人文件放到 `/home`，项目文件放到自己的工作目录，配置和服务文件按系统约定放到对应位置。

## `/home`（home directory，用户主目录）

`/home` 保存普通用户的个人目录。

如果用户名是 `alice`，她的主目录通常是：

```text
/home/alice
```

常见用途：

- 保存文档、下载内容、代码项目
- 存放用户自己的配置文件，例如 `.bashrc`、`.ssh/config`
- 作为日常工作的默认位置

`~` 通常表示当前用户的主目录。例如 `~/project` 等价于 `/home/当前用户名/project`。

## `/root`（root user's home directory，root 用户主目录）

`/root` 是 `root`（root user，超级管理员用户）的主目录，不是普通用户的目录。

普通用户自己的目录在 `/home/用户名`。只有在进行系统维护或排查管理员环境问题时，才通常会接触 `/root`。

## `/etc`（etcetera，系统配置目录）

`/etc` 保存系统和服务的配置文件。这里的文件通常是文本文件，可以用编辑器查看和修改。

常见文件和目录：

```text
/etc/hosts
/etc/fstab
/etc/ssh/sshd_config
/etc/systemd/system
```

修改 `/etc` 下的配置前，建议先备份：

```bash
sudo cp /etc/hosts /etc/hosts.bak
```

这里的 `sudo`（superuser do）表示用管理员权限执行，`cp`（copy）表示复制。

## `/bin`（binaries，基础可执行程序目录）

`/bin` 保存基础命令程序，例如 `ls`（list）、`cp`（copy）、`mv`（move）、`cat`（concatenate）等。

这些命令是系统基本操作所需的工具。很多现代发行版会把 `/bin` 链接到 `/usr/bin`，这是正常现象。

## `/sbin`（system binaries，系统管理程序目录）

`/sbin` 保存系统管理相关命令，常用于启动、修复、网络配置、磁盘维护等场景。

常见命令可能包括：

```text
ip
reboot
shutdown
fsck
```

其中一部分命令需要管理员权限。

## `/usr`（Unix System Resources，用户级系统资源目录）

`/usr` 保存大量用户级程序、库文件、文档和共享资源。它不是普通用户主目录，普通用户主目录是 `/home`。

常见子目录：

- `/usr/bin`（Unix System Resources binaries）：大多数普通命令
- `/usr/sbin`（Unix System Resources system binaries）：系统管理命令
- `/usr/lib`（libraries）：程序库文件
- `/usr/share`（shared data）：共享数据、文档、图标、手册等
- `/usr/local`（local software）：本机手动安装的软件

如果一个软件不是通过系统包管理器安装，而是手动编译安装，常见位置是 `/usr/local`。

## `/var`（variable files，可变数据目录）

`/var` 保存运行过程中经常变化的数据，例如日志、缓存、队列、数据库文件、服务数据等。

常见子目录：

- `/var/log`（logs）：日志文件
- `/var/cache`（cache）：缓存
- `/var/tmp`（temporary files）：跨重启保留时间更长的临时文件
- `/var/lib`（variable libraries）：服务状态数据，例如数据库或包管理器数据
- `/var/www`（web data）：部分 Web 服务的默认站点目录

排查问题时，`/var/log` 是非常常用的位置。

## `/tmp`（temporary files，临时文件目录）

`/tmp` 保存临时文件。程序和用户都可能在这里放短期使用的数据。

注意点：

- `/tmp` 可能在重启后被清理
- 不要在这里长期保存重要文件
- 某些程序会在 `/tmp` 下创建运行时文件

## `/dev`（devices，设备文件目录）

`/dev` 保存设备文件。Linux 把很多设备也抽象成文件，例如硬盘、分区、终端、随机数设备。

常见例子：

- `/dev/sda`：常见磁盘设备名
- `/dev/nvme0n1`：NVMe 磁盘设备名
- `/dev/null`：丢弃所有写入内容的特殊设备
- `/dev/tty`：终端设备

通常不需要手动修改 `/dev` 下的文件，但理解它有助于学习磁盘、挂载和重定向。

## `/proc`（process information，进程和内核信息目录）

`/proc` 是一个虚拟文件系统，用来展示进程和内核状态。它里面的内容不是普通磁盘文件，而是系统运行时生成的信息。

常见文件：

```text
/proc/cpuinfo
/proc/meminfo
/proc/1
```

例如查看 CPU 信息：

```bash
cat /proc/cpuinfo
```

这里的 `cat`（concatenate）表示输出文件内容。

## `/sys`（system information，系统设备信息目录）

`/sys` 也是虚拟文件系统，主要展示内核、硬件设备、驱动和系统状态。

它常用于硬件、驱动、电源、设备树相关的查看和调试。日常使用中一般只读，不随意写入。

## `/run`（runtime data，运行时数据目录）

`/run` 保存系统启动后产生的运行时数据，例如进程 ID 文件、套接字文件、服务状态文件。

常见例子：

```text
/run/sshd.pid
/run/user/1000
```

这些内容通常在重启后重新生成。

## `/boot`（boot files，启动文件目录）

`/boot` 保存系统启动所需文件，例如内核、initramfs、引导程序配置。

常见文件可能包括：

```text
vmlinuz
initrd.img
grub
```

不要随意删除 `/boot` 中的文件，否则可能导致系统无法启动。

## `/lib`、`/lib64`（libraries，系统库目录）

`/lib` 和 `/lib64` 保存系统启动和基础命令运行所需的共享库文件。

普通使用中不需要手动管理这些目录。安装、升级、删除库文件通常交给包管理器处理。

## `/opt`（optional software，可选软件目录）

`/opt` 常用于安装第三方独立软件。

例如某些商业软件或大型工具可能安装到：

```text
/opt/example-app
```

它适合放“不是发行版标准包，但又希望独立管理”的软件。

## `/mnt`（mount，临时挂载目录）和 `/media`（media，可移动媒体目录）

挂载是把磁盘、分区、U 盘、网络存储接到目录树上的过程。

常见用法：

- `/mnt`：手动临时挂载
- `/media`：桌面系统自动挂载 U 盘、移动硬盘等

例如可以把一个分区挂载到 `/mnt/data`，之后访问 `/mnt/data` 就是在访问那个分区。

## `/srv`（service data，服务数据目录）

`/srv` 用于保存服务对外提供的数据，例如网站、FTP、版本库数据等。

并不是每个系统都会使用 `/srv`。如果团队或发行版已有约定，优先遵循现有约定。

## 相对路径、绝对路径和常用符号

绝对路径从 `/` 开始：

```text
/etc/hosts
/home/alice/project
```

相对路径从当前目录开始：

```text
project
../notes
./run.sh
```

常见符号：

- `.`：当前目录
- `..`：上一级目录
- `~`：当前用户主目录
- `/`：路径分隔符，也是根目录

## 目录选择建议

- 个人文件、代码、下载内容：放在 `/home/用户名`
- 系统配置：查 `/etc`
- 服务日志：查 `/var/log`
- 临时文件：放 `/tmp`，但不要长期保存
- 手动安装的本机软件：通常放 `/usr/local` 或 `/opt`
- 外接磁盘或临时挂载：通常用 `/mnt` 或 `/media`

理解目录结构的重点不是背名字，而是知道“这类文件通常在哪里”。这样遇到配置、日志、程序、磁盘、服务问题时，就能快速定位方向。
