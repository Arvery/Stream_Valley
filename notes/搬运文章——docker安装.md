以下内容源于腾讯开悟使用手册（https://doc.aiarena.tencent.com/competition/2.1.0/competition-platform/enter-exp/），个人亲测有效，docker可以顺利使用，放这里做文档记录。

### 2.2 容器工具[](https://doc.aiarena.tencent.com/competition/2.1.0/aiarena-client/get-started/#22-容器工具)

在腾讯开悟客户端中，启动开发或训练环境需要容器工具在电脑后台运行。以下以Docker为例进行介绍。

#### Windows系统安装[](https://doc.aiarena.tencent.com/competition/2.1.0/aiarena-client/get-started/#windows系统安装)

下边将介绍在Windows系统下，如何进行Docker的安装使用。因低版本Docker可能会运行出错，安装版本需大于**24.0.0**。如希望了解更多关于Docker的内容，请参考[Docker官网文档](https://docs.docker.com/)。

**a) 下载安装包**

官网下载链接：https://www.docker.com/get-started/

**b) 进行安装**

在官网下载安装包后，即可按照以下流程进行安装。

> 如在安装过程中遇到问题，请前往[Docker安装问题](https://doc.aiarena.tencent.com/competition/2.1.0/Q&A/docker-install/)查找解决方案。

1. 打开下载完成的安装包，按照默认勾选选项安装。

![docker_install1](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/docker_install1-f29d88cc3e015df7d1a6c0cb1b171add.png)

1. 安装完成之后，桌面打开Docker Desktop客户端。初次运行需点击【Accept】同意协议，之后点击【Skip】跳过Docker调研，即可开始运行。

![docker_install2](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/docker_install2-4edbd1f1c7eaaf9fc2aa11ac174ba3f9.png)![docker_install3](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/docker_install3-19cee770178cf6d50178389eb81baf09.png)

1. 打开docker并等待一段时间后，你可以在左下角看到docker状态是运行中（running），此时表示docker已经启动完成了。 （**注意：使用客户端本地开发或训练时，需保持docker在后台运行。**）

![docker_running](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/docker_running-794c0cba8d71620cd67a9158eabbf2dd.png)

**c) 更新WSL 2内核**

若初次运行docker后，可能出现下图提示，则需要更新WSL 2内核。请按照以下步骤进行

![docker_install4](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/docker_install4-f050d9dfe0d3a86f89924cb9f95f4a9c.png)

1. 访问弹窗中提示的网站（中文页面可[点此查看](https://docs.microsoft.com/zh-cn/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)），在打开的页面找到步骤4，并下载下图所示的安装包。

![wsl-1](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/wsl-1-8027878a9957f1e726d943043dce9ac5.png)

1. 下载完毕后，运行WSL安装包。

![wsl-2](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/wsl-2-f8e3abb667cd5050b8c712d4daa7b2fe.png)![wsl-3](https://doc.aiarena.tencent.com/competition/2.1.0/assets/images/wsl-3-98760ab9c5d088d5a39a4836c77f3e89.png)

1. 安装完毕之后，点击Finish。

![wsl-4](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/wsl-4-624eefcc42089e522708126a2eb3b6aa.png)

1. 打开Windows系统终端。你可以按下 `Windows 键+R` 组合键打开运行窗口，在运行窗口中输入 `cmd` 并回车，此时会打开 Windows 系统终端。（另外，你也可以在电脑的左下角搜索框中搜索“命令提示符”，然后点击搜索结果进入终端。）

![wsl-6](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/wsl-6-a0fa8f7b67cbbf35d7bf83f9aca26005.png)

1. 将WLS 2设置为默认版本。点击复制下方命令，然后在终端中，粘贴刚才复制的代码，点击回车。此时，会在终端内看到 `操作成功完成` 提示语。

```powershell
wsl --set-default-version 2
```



![wsl-8](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/wsl-8-1429ae9b50c23feed9f8c2c6aff39757.png)

1. 最后，进行wsl更新。同样在终端内输入下方命令，点击回车完成操作。（**注意：Windows11系统务必执行此操作**）

```powershell
wsl --update
```



如希望了解更多关于WSL 2的内容，请参考[微软官方文档](https://docs.microsoft.com/zh-cn/windows/wsl/install-manual)。

#### macOS安装[](https://doc.aiarena.tencent.com/competition/2.1.0/aiarena-client/get-started/#macos安装)

1. 通过Docker官网来下载安装程序。
2. 双击Docker.dmg文件以打开安装程序，接着将Docker图标拖动至“Applications”文件夹。默认情况下，Docker Desktop将安装在/Applications/Docker.app。

![docker-install-mac](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/docker-install-mac-34d721f576fe1177c4966c704f3462cd.png)

1. 启动Docker，方法是双击位于“Applications”文件夹中的Docker.app。第一次启动可能提示：“Docker”是从互联网下载的App。你确定要打开它吗？选择打开。

![security-remind](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/security-remind-dda2db9b31142fd85131255cc73b1682.png)

1. Docker菜单将显示Docker订阅服务协议。若要继续，请选择接受该协议。

请注意，若你不接受这些条款，Docker Desktop将无法运行。你可以稍后打开Docker Desktop以接受这些条款。

![docker-accept](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/docker-accept-fc7e0f5a9ab5046ac3d6a6db99134a4a.png)

1. 在安装窗口中，选择以下选项（建议选择推荐设置）：
   - 使用推荐设置（需要密码）：这将使Docker Desktop自动配置所需的设置。
   - 使用高级设置：在此选项下，你可以自定义Docker CLI工具的位置（有关详细信息，请参阅设置），在系统或用户目录中设置，启用默认Docker套接字以及启用特权端口映射。

![docker-setting](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/docker-setting-77e8ac7ac059fad81358f71a4593e4d9.png)

1. 单击“完成”。如果在步骤5中选择了需要密码的配置，请输入你的密码以确认所选设置。随后就可以打开Docker Desktop了，点击最下方的跳过登录按钮即可进入主页面。

![docker-home](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/docker-home-d1b540ab67823060ae0197701091462c.png)