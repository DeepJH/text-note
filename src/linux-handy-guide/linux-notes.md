# Linux 实用知识简明指南

掌握目录和命令之后，还需要理解一些系统层面的概念。它们不一定复杂，但会频繁出现在软件安装、服务部署、日志排查、权限处理和远程连接中。

## 发行版和包管理

Linux 不是单一系统，而是一类系统。常见发行版包括 Ubuntu、Debian、Fedora、Arch Linux、openSUSE、Alpine 等。它们使用相同或相近的 Linux 内核，但软件包格式、默认工具和配置习惯可能不同。

查看当前发行版：

```bash
cat /etc/os-release
```

这里的 `cat`（concatenate）表示输出文件内容，`/etc`（etcetera）是系统配置目录。

常见包管理工具：

```bash
sudo apt update
sudo apt install curl
sudo dnf install curl
sudo pacman -S curl
sudo apk add curl
```

- `apt`（Advanced Package Tool）：Debian、Ubuntu 常用
- `dnf`（Dandified YUM）：Fedora、RHEL 系常用
- `pacman`（package manager）：Arch Linux 常用
- `apk`（Alpine Package Keeper）：Alpine Linux 常用
- `curl`（Client URL）：常用网络请求工具
- `sudo`（superuser do）：用管理员权限执行命令

安装软件前，先确认发行版和包管理工具，避免把不同发行版的命令混用。

## 用户、组和权限

Linux 是多用户系统。文件通常有所有者、所属组和权限。

查看当前用户：

```bash
whoami
id
```

- `whoami`（who am I）：显示当前用户名
- `id`（identity）：显示用户 ID、组 ID 和所属组

查看文件权限：

```bash
ls -l
```

示例：

```text
-rw-r--r-- 1 alice dev 120 May 15 note.txt
```

可以这样读：

- 第一个字符：文件类型，`-` 表示普通文件，`d` 表示目录
- `rw-`：所有者权限
- `r--`：所属组权限
- `r--`：其他用户权限
- `alice`：所有者
- `dev`：所属组

权限含义：

- `r`（read）：读
- `w`（write）：写
- `x`（execute）：执行；对于目录表示可以进入

常见权限值：

- `644`：文件常用，所有者可读写，其他人只读
- `755`：脚本或目录常用，所有者可读写执行，其他人可读可执行
- `600`：私钥等敏感文件常用，只有所有者可读写

## `sudo` 和管理员权限

`sudo`（superuser do）用于临时以管理员权限执行命令。

常见场景：

```bash
sudo apt install nginx
sudo systemctl restart nginx
sudo cp config.conf /etc/example.conf
```

`sudo` 很方便，但也能修改系统关键文件。执行前应确认三件事：

- 命令会修改哪里
- 是否有备份或回滚方式
- 路径是否写对，尤其是删除、覆盖、递归操作

## Shell、终端和配置文件

终端是输入命令的界面，Shell 是解释命令的程序。常见 Shell：

- `bash`（Bourne Again Shell）
- `zsh`（Z Shell）
- `fish`（friendly interactive shell）

查看当前 Shell：

```bash
echo $SHELL
```

常见配置文件：

- `~/.bashrc`：Bash 交互式 Shell 配置
- `~/.profile`：登录环境配置
- `~/.zshrc`：Zsh 配置
- `~/.ssh/config`：SSH 客户端配置

修改 Shell 配置后，可以重新打开终端，或执行：

```bash
source ~/.bashrc
```

`source`（source script）表示在当前 Shell 中读取并执行脚本。

## 环境变量和 `PATH`

环境变量会影响程序运行方式。查看全部环境变量：

```bash
env
```

`env`（environment）表示查看或设置环境变量。

查看某个变量：

```bash
echo $PATH
```

`PATH`（path）决定 Shell 去哪些目录寻找命令。例如你输入 `python`，系统会按 `PATH` 中的目录顺序查找可执行文件。

临时设置变量：

```bash
export APP_ENV=production
```

`export`（export variable）让变量对子进程可见。临时设置只在当前终端会话有效；想长期生效，可以写入 `~/.bashrc` 或对应 Shell 配置文件。

## 服务和 `systemd`

很多后台程序以服务形式运行，例如 SSH、Nginx、数据库、定时任务代理等。现代 Linux 发行版常用 `systemd` 管理服务。

查看服务状态：

```bash
systemctl status ssh
```

常见操作：

```bash
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl enable nginx
sudo systemctl disable nginx
```

- `systemctl`（system control）：管理系统服务
- `start`：启动
- `stop`：停止
- `restart`：重启
- `enable`：设置开机自启
- `disable`：取消开机自启
- `ssh`（Secure Shell）：远程登录服务

服务出问题时，通常先看 `systemctl status 服务名`，再看日志。

## 日志和 `journalctl`

日志是排查问题的重要入口。传统日志通常位于：

```text
/var/log
```

`/var`（variable files）保存可变数据，`/var/log`（logs）保存日志。

查看文件日志：

```bash
tail -f /var/log/syslog
```

`tail -f`（tail, follow）会持续显示新增内容。

查看 `systemd` 日志：

```bash
journalctl -u nginx
journalctl -u nginx -f
journalctl -xe
```

- `journalctl`（journal control）：查看 systemd 日志
- `-u`（unit）：指定服务单元
- `-f`（follow）：持续跟随输出
- `-xe`：显示当前相关错误和上下文

常见排查顺序：

1. 查看服务状态：`systemctl status 服务名`
2. 查看服务日志：`journalctl -u 服务名`
3. 查看应用自己的日志文件
4. 检查配置文件和权限

## 网络基础

查看 IP 地址：

```bash
ip addr
```

查看路由：

```bash
ip route
```

测试域名或地址连通：

```bash
ping example.com
```

访问 URL 或接口：

```bash
curl https://example.com
```

查看监听端口：

```bash
ss -tulpn
```

- `ip`（IP utility）：查看和配置网络
- `ping`（packet internet groper）：测试网络连通
- `curl`（Client URL）：访问 URL
- `ss`（socket statistics）：查看网络连接和端口

网络问题可以按这个顺序看：

1. 本机有没有 IP
2. 路由是否正常
3. DNS 是否能解析域名
4. 目标端口是否开放
5. 防火墙或安全组是否拦截

## SSH 和远程连接

`ssh`（Secure Shell）用于远程登录服务器：

```bash
ssh user@example.com
```

常见 SSH 文件：

- `~/.ssh/id_rsa`：私钥
- `~/.ssh/id_rsa.pub`：公钥
- `~/.ssh/authorized_keys`：允许登录的公钥列表
- `~/.ssh/config`：SSH 客户端配置
- `/etc/ssh/sshd_config`：SSH 服务端配置

私钥权限通常需要比较严格：

```bash
chmod 600 ~/.ssh/id_rsa
```

`chmod`（change mode）用于修改权限，`600` 表示只有所有者可读写。

复制文件到远程：

```bash
scp file.txt user@example.com:/tmp/
rsync -av project/ user@example.com:/tmp/project/
```

- `scp`（secure copy）：通过 SSH 复制文件
- `rsync`（remote sync）：同步文件，适合目录和增量传输

## 文件系统、磁盘和挂载

查看磁盘空间：

```bash
df -h
```

查看目录占用：

```bash
du -sh *
```

查看磁盘和分区：

```bash
lsblk
```

- `df`（disk free）：查看文件系统可用空间
- `du`（disk usage）：查看文件或目录占用
- `lsblk`（list block devices）：查看块设备

挂载的意思是把某个磁盘、分区或网络存储接到目录树中的某个位置。常见挂载点包括 `/mnt`（mount）和 `/media`（media）。

开机自动挂载通常配置在：

```text
/etc/fstab
```

修改 `/etc/fstab` 前应备份，因为错误配置可能影响系统启动或挂载。

## 压缩包和归档

Linux 中常见两类操作：

- 打包：把多个文件合成一个文件
- 压缩：减少文件体积

`tar`（tape archive）常用于打包，也可以配合 gzip 压缩：

```bash
tar -czf project.tar.gz project/
tar -xzf project.tar.gz
```

`zip` 和 `unzip` 常用于 `.zip` 文件：

```bash
zip -r project.zip project/
unzip project.zip
```

## 文本编辑器

服务器上常见终端编辑器：

- `nano`（Nano's ANOther editor）：操作直接，适合快速改文件
- `vim`（Vi IMproved）：功能强，适合大量文本编辑

用 `nano` 编辑：

```bash
nano config.txt
```

常用按键：

- `Ctrl + O`：保存
- `Ctrl + X`：退出
- `Ctrl + W`：搜索

`vim` 的最低限度操作：

- `i`：进入插入模式
- `Esc`：回到普通模式
- `:wq`：保存并退出
- `:q!`：不保存退出

## 常见错误类型

命令报错时，先判断属于哪一类：

- `command not found`：命令不存在，可能没安装，或不在 `PATH`
- `No such file or directory`：路径不存在或写错
- `Permission denied`：权限不足，或文件没有执行权限
- `Address already in use`：端口已被占用
- `Connection refused`：目标地址可达，但服务没监听或被拒绝
- `No space left on device`：磁盘空间不足

对应处理方向：

- 查命令：`command -v 命令名`
- 查路径：`ls -l 路径`
- 查权限：`ls -l`
- 查端口：`ss -tulpn`
- 查磁盘：`df -h`
- 查日志：`journalctl` 或 `/var/log`

## 学习和使用建议

更有效的学习顺序：

1. 目录结构和路径
2. 文件操作、查看、搜索
3. 权限、用户、`sudo`
4. 包管理和服务管理
5. 日志、网络、SSH
6. Shell 配置、环境变量、脚本

Linux 的优势在于组合能力。单个命令不一定复杂，关键是理解输入、输出、文件、进程、权限和管道之间的关系。
