
SSH 密钥的生成方式如下：

*   ED25519 密钥，请查看[ED25519 SSH 密钥](#ed25519-ssh-keys)
*   RSA 密钥，请查看[RSA SSH 密钥](#rsa-ssh-keys) 

### ED25519 SSH keys

[Practical Cryptography With Go](https://leanpub.com/gocrypto/read#leanpub-auto-chapter-5-digital-signatures) 一书中表明 [ED25519](https://ed25519.cr.yp.to/) 密钥比 RSA 密钥更为安全。

2014年 OpenSSH 6.5 引入 ED25519 SSH 密钥后，当前任何操作系统都可用使用这种密钥。

你可以使用以下命令创建和配置 ED25519 密钥：

```
ssh-keygen -t ed25519 -C "<comment>" 
```

`-C`（例如带引号注释的电子邮件地址）是标记 SSH 密钥的可选方法。

你将看到类似于以下内容的响应：

```
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/user/.ssh/id_ed25519): 
```

要获得指导，请继续执行[常见步骤](#common-steps-for-generating-an-ssh-key-pair) .

### RSA SSH 密钥

如果你使用 RSA 密钥生成 SSH 密钥，则我们建议你至少使用 [ 2048 位](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57Pt3r1.pdf)的密钥大小. 默认情况下， `ssh-keygen`命令创建一个 1024 位 RSA 密钥.

你可以使用以下命令创建和配置 RSA 密钥，如果需要，可以生成建议的最小密钥大小`2048`：

```bash
ssh-keygen -t rsa -b 2048 -C "email@example.com" 
```

`-C`标志（例如带引号注释的电子邮件地址）是标记 SSH 密钥的可选方法。

你将看到类似于以下内容的响应：

```bash
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa): 
```

要获得指导，请继续执行[常见步骤](#common-steps-for-generating-an-ssh-key-pair) 。

**注意：** 如果你使用 7.8 或更低版本的 OpenSSH，请参考与[编码](#rsa-keys-and-openssh-from-versions-65-to-78)相关的问题。

### SSH 密钥生成步骤

无论是创建[ED25519](#ed25519-ssh-keys)还是创建[RSA](#rsa-ssh-keys)密钥，你都从`ssh-keygen`命令开始。此时，你将在命令行中看到以下消息（以 ED25519 密钥为例）：

```bash
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa): 
```

如果你还没有 SSH 密钥对并且也没有生成[部署密钥](#deploy-keys) ，你可以按照系统提示的建议选择 SSH 密钥存储的文件和目录，SSH 客户端将使用默认配置来生成你的 SSH 密钥。

当然，你也可以将新生成的 SSH 密钥保存在其他位置。你可以选择要分配的目录和文件名，你还可以为专用的[特定主机](#working-with-non-default-ssh-key-pair-paths) 生成SSH 密钥。

在选择 SSH 密钥的保存路径后，你可以为 SSH 密钥设置[密码](https://www.ssh.com/ssh/passphrase/) ：

```bash
Enter passphrase (empty for no passphrase):
Enter same passphrase again: 
```

如果成功，你将看到有关`ssh-keygen`命令将标识和私钥保存在何处的确认信息。

如有需要，你也可以使用以下命令更新密码：

```bash
ssh-keygen -p -f /path/to/ssh_key 
```

### OpenSSH 6.5 ~ 7.8 的 RSA 密钥

在 OpenSSH 7.8 之前，RSA 密钥的默认公共密钥指纹基于 MD5，因此并不安全。

如果你的 OpenSSH 版本介于 6.5 至 7.8（含）之间，请使用`-o`选项运行`ssh-keygen` ，以更安全的 OpenSSH 格式保存你的 SSH 私钥。

如果你已经具有可用于 GitCode 的 RSA SSH 密钥，请考虑对其进行升级以使用更安全的密码加密格式。 你可以使用以下命令进行操作：

```bash
ssh-keygen -o -f ~/.ssh/id_rsa 
```

或者，你可以使用以下命令以更安全的加密格式生成新的 RSA 密钥：

```bash
ssh-keygen -o -t rsa -b 4096 -C "email@example.com" 
```

**注意：** ED25519 已将密钥加密为更安全的 OpenSSH 格式。

## 在你的 GitCode 账号中添加 SSH 密钥

现在，你可以将创建好的 SSH 密钥复制到你的 GitCode 帐户。你可以参考以下步骤：

1. **复制公钥**：从以文本格式保存 SSH 密钥的位置复制你的**公共** SSH 密钥，以下命令可以将 ED25519 的信息保存到指定操作系统的剪贴板中：

    **macOS:**

    ```bash
    pbcopy < ~/.ssh/id_ed25519.pub 
    ```

    **Linux（需要 xclip 软件包）：**

    ```bash
    xclip -sel clip < ~/.ssh/id_ed25519.pub 
    ```

    **Windows 上的 Git Bash：**

    ```bash
    cat ~/.ssh/id_ed25519.pub | clip 
    ```

    如果你使用的是 RSA 密钥，相应地替换即可。

1. **登录GitCode**：首先，请确保你已登录到GitCode帐户
2. **进入设置**：点击页面右上角的头像，选择“个人设置”
3. **选择公钥管理**：在左侧导航栏中，选择“公钥管理- SSH 公钥”选项卡
4. **添加公钥**：点击「+ SSH 公钥」按钮
5. **本地生成 SSH 公钥**：按照指南生成 SSH 公钥，这通常涉及在本地系统上运行一些命令以生成密钥对（公钥和私钥）
6. **添加公钥**：将生成的SSH公钥粘贴到“公钥”字段中，并为密钥提供一个描述性标题
7. **创建 SSH 公钥**：点击「新建」按钮以保存 SSH 公钥

**注意：** 如果你手动复制了公共 SSH 密钥，请确保复制了整个密钥，以`ssh-ed25519` （或`ssh-rsa` ）开头，并以你的电子邮件地址结尾。

### 测试 SSH 密钥是否能够正常工作

要测试是否正确添加了 SSH 密钥，可以在终端中运行以下命令：

```bash
ssh -T git@gitcode.com
```

在你第一次通过 SSH 方式连接到 GitCode的时候，将会询问你是否信任将要连接的 GitCode host地址。当确认 `yes` 后，会将 GitCode 作为已知主机添加到受信任的 hosts 地址中：

```bash
The authenticity of host 'gitcode.com (121.36.6.22)' can't be established.
ECDSA key fingerprint is SHA256:HbW3g8zUjNSksFbqTiUWPWg2Bq1x8xdGUrliXFzSnUw.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'gitcode.com' (ECDSA) to the list of known hosts. 
```

一旦添加到已知主机列表中，将不再要求你再次验证 GitCode 主机的真实性。 再次运行以上命令时，你将只收到*欢迎使用 GitCode 的`@username` ！* 信息。

如果未出现欢迎消息，则可以通过使用以下命令在详细模式下运行`ssh`来解决问题：

```bash
ssh -Tv git@gitcode.com 
```

### 使用非默认路径的 SSH 密钥

如果你为 SSH 密钥对使用了非默认文件路径，请配置 SSH 客户端以指向 GitCode 私有 SSH 密钥。

可以运行以下命令进行配置：

```bash
eval $(ssh-agent -s)
ssh-add <path to private SSH key> 
```

以上设置将会保存到`~/.ssh/config`文件中。以下是两个专用于 GitCode 的 SSH 密钥示例：

```bash
# GitCode
  Host gitcode.com
  Preferredauthentications publickey
  IdentityFile ~/.ssh/gitcode_rsa

# Github instance
  Host github.com
  Preferredauthentications publickey
  IdentityFile ~/.ssh/example_github_rsa 
```

公共 SSH 密钥对于 GitCode 必须是唯一的，因为它们将绑定到你的账号中。 SSH 密钥是通过 SSH 推送代码时唯一的标识符，这是为什么它需要唯一地映射到单个用户的原因。

### 为项目设置 SSH 密钥

如果要根据正在使用的项目代码仓库使用不同的密钥，则可以在代码仓库中执行以下命令：

```bash
git config core.sshCommand "ssh -o IdentitiesOnly=yes -i ~/.ssh/private-key-filename-for-this-repository -F /dev/null" 
```

这不使用 SSH 代理，并且至少需要 Git 2.10.

### 多账号设置

[为项目设置 SSH 密钥](#per-repository-ssh-keys)方法还适用于在 GitCode 中使用多个账号的情况。

此外，你也可以直接在`~.ssh/config`为主机分配别名。 如果在`.ssh/config`中的`Host`块之外设置了`IdentityFile` ，则 SSH 和作为扩展的 Git 将无法登录. 这是 SSH 组装`IdentityFile`条目的方式，因此不能通过将`IdentitiesOnly`设置为`yes`来更改. `IdentityFile`条目应指向 SSH 密钥对的私钥。

**注意：**私钥和公钥应仅由用户读取，通过运行以下`chmod 0400 ~/.ssh/<example_ssh_key>`在 Linux 和 macOS 上完成此操作： `chmod 0400 ~/.ssh/<example_ssh_key>`和`chmod 0400 ~/.ssh/<example_sh_key.pub>` 。

```bash
# User1 Account Identity Host <user_1.gitcode.com>
  Hostname gitcode.com
  PreferredAuthentications publickey
  IdentityFile ~/.ssh/<example_ssh_key1>

# User2 Account Identity Host <user_2.gitcode.com>
  Hostname gitcode.com
  PreferredAuthentications publickey
  IdentityFile ~/.ssh/<example_ssh_key2> 
```

**注意：** 为提高效率和透明度，示例`Host`别名定义为`user_1.gitcode.com`和`user_2.gitcode.com` 。 高级配置难以维护，使用这种别名在使用其他工具（如`git remote`子命令）时会更容易理解。 SSH 可以将任何字符串理解为`Host`别名，因此`Tanuki1`和`Tanuki2`尽管提供了很少的上下文指向它们，也可以使用.

克隆`GitCode`代码仓库通常如下所示：

```bash
git clone git@ggitcode.com:repo-org/repo.git 
```

要为`user_1`克隆它，请将`gitcode.com`替换为 SSH 别名`user_1.gitcode.com` ：

```bash
git clone git@<user_1.gitcode.com>:repo-org/repo.git 
```

使用`git remote`命令可以修复以前克隆的代码仓库。

以下的示例假定远程代码仓库被别名为`origin`：

```bash
git remote set-url origin git@<user_1.gitcode.com>:repo-org/repo.git 
```

#### Eclipse

如果使用的是[EGit](https://www.eclipse.org/egit/) ，则可以[将 SSH 密钥添加到 Eclipse](https://wiki.eclipse.org/EGit/User_Guide#Eclipse_SSH_Configuration) .

#### Windows系统

如果你运行的是 Windows 10， [适用于 Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10)的[Windows 子系统（WSL）](https://docs.microsoft.com/en-us/windows/wsl/install-win10)及其最新的[WSL 2](https://docs.microsoft.com/en-us/windows/wsl/install-win10#update-to-wsl-2)版本，则支持安装不同的 Linux 发行版，其中包括 Git 和 SSH 客户端。

对于当前版本的 Windows，你还可以通过[Git for Windows](https://gitforwindows.org)安装 Git 和 SSH 客户端。

替代工具包括：

*   [Cygwin](https://www.cygwin.com)
*   [PuttyGen](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)

### 故障排除

如果在 Git Clone 上，系统会提示你输入密码，例如`git@gitcode.com's password:`，则表明你的 SSH 设置有问题。

*   确保你正确地生成了 SSH 密钥，并将公共 SSH 密钥添加到了你 GitCode 账号的 SSH 密钥中
*   尝试使用`ssh-agent`手动注册你的私有 SSH 密钥，如本文档前面所述
*   尝试通过运行`ssh -Tv git@gitcode.com`调试连接