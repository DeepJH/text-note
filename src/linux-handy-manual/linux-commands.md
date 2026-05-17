# Linux 常用命令简明指南

Linux 命令的学习重点不是记住所有参数，而是理解常用命令解决什么问题、常见选项怎么组合。下面按使用场景整理，示例都保持为可直接复制运行的形式。

## 路径和目录切换

查看当前目录：

```bash
pwd
```

`pwd`（print working directory）显示当前所在目录的完整路径。

切换目录：

```bash
cd /etc
cd ..
cd ~
cd -
```

`cd`（change directory）用于切换目录。

- `cd /etc`：进入 `/etc`（etcetera，系统配置目录）
- `cd ..`：进入上一级目录
- `cd ~`：回到当前用户主目录
- `cd -`：回到上一次所在目录

## 查看目录内容

```bash
ls
ls -l
ls -a
ls -lh
ls -lt
```

`ls`（list）用于列出目录内容。

- `ls -l`（long format）：显示权限、所有者、大小、时间等详细信息
- `ls -a`（all）：显示隐藏文件
- `ls -lh`（human-readable）：用更容易阅读的单位显示文件大小
- `ls -lt`（time）：按修改时间排序

## 创建文件和目录

```bash
touch note.txt
mkdir docs
mkdir -p project/src/linux
```

- `touch`（touch file）：常用于创建空文件或更新文件时间
- `mkdir`（make directory）：创建目录
- `mkdir -p`（parents）：递归创建多级目录，目录已存在时不报错

## 复制、移动、重命名、删除

```bash
cp a.txt b.txt
cp -r docs docs-backup
mv old.txt new.txt
mv file.txt docs/
rm old.txt
rm -r old-folder
```

- `cp`（copy）：复制文件或目录
- `cp -r`（recursive）：递归复制目录
- `mv`（move）：移动或重命名
- `rm`（remove）：删除文件
- `rm -r`（recursive）：递归删除目录

`rm` 删除后通常不会进入回收站。执行删除前，先确认路径和通配符是否正确。

## 查看文件内容

```bash
cat note.txt
less long.log
head note.txt
head -n 20 note.txt
tail note.txt
tail -n 50 note.txt
tail -f app.log
```

- `cat`（concatenate）：输出文件内容，适合短文件
- `less`（less pager）：分页查看长文件，按 `q` 退出
- `head`（head）：查看文件开头
- `tail`（tail）：查看文件结尾
- `tail -f`（follow）：持续查看文件新增内容，常用于日志

## 查找文件和内容

按文件名查找：

```bash
find . -name "*.md"
find /etc -name "ssh*"
find . -type f -size +10M
```

`find`（find）用于查找文件。

- `-name`（name）：按名称匹配
- `-type f`（file）：只查文件
- `-type d`（directory）：只查目录
- `-size +10M`（size）：查找大于 10 MB 的文件

查找文本内容：

```bash
grep "error" app.log
grep -n "error" app.log
grep -r "TODO" .
```

`grep`（global regular expression print）用于搜索文本。

- `grep -n`（line number）：显示行号
- `grep -r`（recursive）：递归搜索目录
- `grep -i`（ignore case）：忽略大小写

如果系统安装了 `rg`（ripgrep），它通常比 `grep -r` 更快：

```bash
rg "TODO"
rg -n "error" logs/
```

## 文本处理

输出文本：

```bash
echo "hello"
printf "hello\n"
```

- `echo`（echo）：输出文本
- `printf`（print formatted）：按格式输出文本

排序、去重、统计：

```bash
sort names.txt
sort names.txt | uniq
wc -l app.log
```

- `sort`（sort）：排序
- `uniq`（unique）：去掉相邻重复行，通常和 `sort` 搭配
- `wc`（word count）：统计行数、词数、字节数
- `wc -l`（lines）：统计行数

截取列和流式处理：

```bash
cut -d ":" -f 1 /etc/passwd
awk '{print $1}' app.log
sed 's/old/new/g' file.txt
```

- `cut`（cut）：按分隔符截取列
- `awk`（Aho, Weinberger, Kernighan）：按字段处理文本
- `sed`（stream editor）：流式编辑文本

这三个命令功能很强，不需要一次掌握所有语法。先会读简单例子即可。

## 管道和重定向

管道 `|` 把前一个命令的输出交给后一个命令：

```bash
ps aux | grep ssh
ls -lh | less
cat app.log | grep "error"
```

重定向把输出写入文件：

```bash
echo "hello" > note.txt
echo "world" >> note.txt
cat missing.txt 2> error.log
```

- `>`：覆盖写入
- `>>`：追加写入
- `2>`：把错误输出写入文件
- `|`：管道，连接多个命令

## 权限和所有者

查看权限：

```bash
ls -l
```

修改权限：

```bash
chmod +x run.sh
chmod 644 note.txt
chmod 755 script.sh
```

`chmod`（change mode）用于修改权限。

- `+x`（execute）：增加执行权限
- `644`：所有者可读写，其他人只读
- `755`：所有者可读写执行，其他人可读可执行

修改所有者：

```bash
sudo chown alice:alice note.txt
sudo chown -R alice:alice project
```

`chown`（change owner）用于修改文件所有者，`-R`（recursive）表示递归处理目录。

管理员权限：

```bash
sudo systemctl status ssh
```

`sudo`（superuser do）表示用管理员权限执行命令。涉及系统配置、服务、软件安装、系统目录写入时经常需要它。

## 进程和资源

查看进程：

```bash
ps
ps aux
top
```

- `ps`（process status）：查看进程快照
- `ps aux`：查看更完整的进程列表
- `top`（table of processes）：动态查看进程和资源占用

结束进程：

```bash
kill 12345
kill -9 12345
pkill nginx
```

- `kill`（kill process）：向进程发送信号
- `kill -9`：强制结束进程，谨慎使用
- `pkill`（process kill）：按进程名结束进程

查看命令位置：

```bash
which python
command -v python
```

- `which`（which command）：查找命令路径
- `command -v`：Shell 内置方式，常用于脚本判断命令是否存在

## 网络相关

查看网络连通：

```bash
ping example.com
curl https://example.com
```

- `ping`（packet internet groper）：测试网络连通
- `curl`（Client URL）：访问 URL、调用接口、下载内容

查看地址和端口：

```bash
ip addr
ip route
ss -tulpn
```

- `ip`（IP utility）：查看和配置网络
- `ip addr`：查看 IP 地址
- `ip route`：查看路由
- `ss`（socket statistics）：查看端口和连接
- `ss -tulpn`：查看 TCP/UDP 监听端口和进程

远程登录和复制：

```bash
ssh user@example.com
scp file.txt user@example.com:/tmp/
rsync -av project/ user@example.com:/tmp/project/
```

- `ssh`（Secure Shell）：远程登录
- `scp`（secure copy）：通过 SSH 复制文件
- `rsync`（remote sync）：同步文件，适合目录和增量复制

## 压缩和解压

```bash
tar -czf project.tar.gz project/
tar -xzf project.tar.gz
zip -r project.zip project/
unzip project.zip
```

- `tar`（tape archive）：打包文件
- `tar -c`（create）：创建包
- `tar -x`（extract）：解包
- `tar -z`（gzip）：使用 gzip 压缩或解压
- `tar -f`（file）：指定文件名
- `zip`（zip）：创建 zip 压缩包
- `unzip`（unzip）：解压 zip 文件

## 磁盘和空间

查看磁盘空间：

```bash
df -h
du -sh *
du -h --max-depth=1
```

- `df`（disk free）：查看文件系统剩余空间
- `df -h`（human-readable）：用易读单位显示
- `du`（disk usage）：查看目录或文件占用空间
- `du -sh`（summary, human-readable）：汇总显示大小

查看挂载：

```bash
mount
lsblk
```

- `mount`（mount）：查看或执行挂载
- `lsblk`（list block devices）：查看磁盘和分区结构

## 系统信息和时间

```bash
uname -a
hostname
date
uptime
whoami
id
```

- `uname`（Unix name）：查看内核和系统信息
- `hostname`（host name）：查看主机名
- `date`（date）：查看或设置时间
- `uptime`（up time）：查看系统运行时间和负载
- `whoami`（who am I）：查看当前用户名
- `id`（identity）：查看用户 ID、组 ID 和所属组

## 帮助和手册

```bash
man ls
ls --help
type cd
history
```

- `man`（manual）：查看命令手册
- `--help`（help）：查看简短帮助
- `type`（type）：查看命令是内置命令、别名还是外部程序
- `history`（history）：查看历史命令

`man` 页面中常用按键：

- `q`：退出
- `/keyword`：搜索
- `n`：跳到下一个搜索结果

## 常用组合

查找大文件：

```bash
du -h --max-depth=1 | sort -h
```

查看占用某个端口的进程：

```bash
ss -tulpn | grep ":80"
```

持续查看日志中的错误：

```bash
tail -f app.log | grep "error"
```

查找项目中的 TODO：

```bash
rg "TODO" .
```

命令越熟练，越应该关注“输入、输出、组合”。Linux 命令很多都能通过管道连接起来，这也是它高效的原因。
