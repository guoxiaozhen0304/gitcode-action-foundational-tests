
Git LFS 是指 Git 的大文件存储（Large File Storage），是一个用于有效管理大型二进制文件的工具。它允许开发者将大文件从代码仓库中分离出来，比如如图像、音频、视频和数据文件等，将其存储在单独的存储区域，并在存储库中仅保留文件的引用。这样可以避免存储库因每次保存 diff 导致的体积过大，加速存储库的克隆和下载过程，并确保大文件的版本控制不会导致性能问题。

通过 Git LFS，可以实现：

- **分离大文件**：LFS 允许将大文件从代码仓库中分离出来，将其存储在单独的位置
- **版本控制**：LFS 仍然提供版本控制，但仅在存储库中保留文件的引用，以避免存储库过大
- **高性能**：LFS 可以加速存储库的克隆和下载过程，因为它不需要每次都传输大文件
- **文件锁定**：LFS 支持文件锁定，以避免多个用户同时编辑大文件引发冲突

![Git LFS](/images/git-lfs.gif)

### Git LFS 下载和安装

> 注意：安装 Git LFS 需要 Git 的版本不低于 **1.8.5**
>
> Git LFS 官网： <https://git-lfs.github.com/>
>
> GitCode mirror 过来Git LFS的地址：<https://gitcode.com/mirrors/git-lfs/git-lfs>

#### Linux 系统

```bash
$ curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
$ sudo apt-get install git-lfs
$ git lfs install
```

> 运行`git lfs install`，如果显示Git LFS initialized说明安装成功

#### MacOS 系统

1.安装HomeBrew 

```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

2.安装 Git LFS

```bash
$ brew install git-lfs
$ git lfs install
```

#### Windows 系统

1. 下载安装程序 windows installer
2. 运行 windows installer
3. 在命令行执行 `git lfs install`

### 配置

配置我们要与Git LFS关联的文件类型，此信息将添加到.gitattributes 存储库中的 文件中。

将文件类型与Git LFS关联的最简单方法是通过 `git lfs track` 命令。

如将所有 jpg 文件管理到Git LFS：

```bash
$ git lfs track "*.png"
```

该 `.gitattributes` 文件已创建，并包含以下信息：

```bash
*.jpg filter=lfs diff=lfs merge=lfs -text
```

完美！从现在开始，LFS将处理此文件。现在，我们可以按照以前的方式将其添加到存储库中。注意，对其他任何更改`.gitattributes`也必须提交到存储库，就像其它修改一样：

```bash
$ git add .gitattributes
$ git add design-resources/design.psd
$ git commit -m "Add design file"
```
### 常用 Git LFS 命令

查看 git lfs 当前正在跟踪的所有模式的列表

```bash
$ git lfs track
```

查看 git lfs 当前跟踪的文件列表

```bash
$ git lfs ls-files
```

### 取消跟踪并从LFS 删除文件

从lfs取消跟踪特定类型的所有文件，并将其从缓存中删除：

```bash
$ git lfs untrack "*file-type"
$ git rm --cached "*file-type"
```

如果要将这些文件重新添加到常规git跟踪中并提交，可以执行以下操作：

```bash
$ git add "*file-type"
$ git commit -m "restore "*file-type" to git from lfs"
```

### 最佳实践

以下是使用 LFS 功能的最佳实践：

- 仅用于大型二进制文件：只使用 LFS 来管理大型二进制文件，而不是文本文件
- 启用文件锁定：在多人协作环境中，启用文件锁定以防止多个用户同时编辑大文件
- 定期清理不必要的大文件：定期审查存储库，删除不再需要的大文件引用
- 提供文档：向团队成员提供有关如何使用 LFS 的文档或指南，以确保正确使用


> 感谢 @BaiXuePrincess 贡献的关于 Git-LFS 的帮助文档
>
> 项目地址: https://gitcode.net/BaiXuePrincess/git-lfs