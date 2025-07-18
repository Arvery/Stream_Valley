# 每日一文——docker初识

### 一、什么是 Docker？

**Docker 是一个开源的容器化平台**，它能让你用一种标准的方式打包应用程序及其依赖，然后在任何地方运行。

简而言之，它的作用是：

- **轻量级虚拟化**：不像虚拟机那样需要一个完整操作系统，Docker 使用容器技术，只打包程序和必要的库，运行效率高；
- **环境一致性**：你可以在自己的电脑上构建一个镜像，然后部署到服务器，确保“本地能跑、服务器也能跑”；
- **便于部署与扩展**：开发 → 打包成镜像 → 上传到远程仓库 → 快速部署/回滚。

### 二、什么是wsl？

WSL 的全称是：

> **Windows Subsystem for Linux**
>  （中文：Windows 的 Linux 子系统）

------

###### ✅ 它的本质是：

> ⛳ **让你在 Windows 系统中运行 Linux 命令和程序**，不需要安装虚拟机或双系统。

它是微软官方提供的一种机制，让你在 Windows 上运行真正的 Linux。

###### 🧱 WSL 的几个关键特性：

| 特性         | 说明                                      |
| ------------ | ----------------------------------------- |
| 嵌入式       | 不需要虚拟机，直接在 Windows 上运行 Linux |
| 快速         | 启动很快，资源消耗小                      |
| 支持图形界面 | 最新的 WSLg 可以运行 Linux 图形应用       |
| 直接访问硬盘 | 可以访问 C:\、D:\ 等磁盘                  |
| 支持 Docker  | 可以在 WSL 里跑 GPU 加速的深度学习项目    |

------

###### 🧬 WSL 有两个版本

| 名称             | 特点                                                     |
| ---------------- | -------------------------------------------------------- |
| **WSL 1**        | 更轻量，兼容性较低                                       |
| **WSL 2** ✅ 推荐 | 基于虚拟化技术，完全 Linux 内核，支持 Docker 和 GPU 加速 |

### 三、实战：如何把github上的项目直接采用docker部署

#### 场景一：项目含有 Dockerfile（最常见）

###### 🔧 操作步骤如下：

###### 🪜 步骤 1：克隆 GitHub 项目

以docker帮助文档中的项目为例：

```
git clone https://github.com/docker/welcome-to-docker.githttps://github.com/docker/welcome-to-docker.git
```

------

###### 🪜 步骤 2：查看项目里是否有 `Dockerfile`

```
ls
```

以上命令针对Linux系统

你应该能看到：

![image-20250717232002006](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/image-20250717232002006.png)

如果没有 `Dockerfile`，你就不能直接构建镜像，得自己写。

------

###### 🪜 步骤 3：构建镜像

在VS code命令行下输入

```
docker pull node:18-alpine

docker build -t welcome-to-docker .
```

解释：

国内需要先pull一下基础环境，否则直接build会报网络连接的错误。

- `.` 表示当前目录的 Dockerfile
- `-t welcome-to-docker` 给镜像起名叫 `welcome-to-docker`

------

###### 🪜 步骤 4：运行镜像生成容器（指定端口）

![image-20250717232244631](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/image-20250717232244631.png)

项目运行在容器内的 `80` 端口：

```
docker run -d -p 8080:80 welcome-to-docker
```

解释：

- `-d` 表示后台运行
- `-p 8080:3000` 映射本机的 8080 到容器内部的 80
- 你访问 `http://localhost:8080` 就能访问项目了！

#### 场景二：项目含有 `docker-compose.yml`

这种情况更简单（自动构建并运行）

###### 🪜 步骤 1：克隆项目

```
git clone https://github.com/someone/someproject.git
cd someproject
```

###### 🪜 步骤 2：直接启动服务

```
docker compose up -d
```

或者：

```
docker-compose up -d
```

（根据你系统安装的版本而定）

这一步自动完成：

- 拉取镜像或构建镜像
- 创建并启动多个容器（如 web + db）

场景三：没有Dockerfile的情况

GPT声称它可以为没有dokerfile的项目写dockerfile，亲测了一下是有问题的，不知道是不能给没有dockerfile的写还是说需要有些条件，不知道有没有友友知道能不能给没有dockerfile的项目自己写一个dockerfile免去部署环境的烦恼。

对于dokerfile的构成还需要研究下。深入来讲就是为自己的项目写Dockerfile，先暂且到这里。

### 四、关于无后缀文件的小track

###### 方法一：用记事本创建

1. 打开记事本
2. 写相关内容
3. 点击 `文件 → 另存为`
4. 在弹窗中注意：
   - 文件名填写：`"Dockerfile"`（必须带英文双引号，**防止系统自动加 `.txt` 后缀**）
   - 保存类型选：**所有文件**
   - 编码选：UTF-8

📌 关键是 **带上双引号**，否则保存完会变成 `Dockerfile.txt`

###### 方法二：使用 PowerShell 创建

在你要放置的目录打开 PowerShell，运行：

```
New-Item Dockerfile -ItemType File
```

然后用 VS Code 或记事本编辑这个文件。

###### 方法三：使用 Visual Studio Code

1. 打开 VS Code，进入你的项目目录
2. 在左边文件树中右键 → New File
3. 输入文件名：`Dockerfile`（不要加后缀）
4. 输入内容并保存即可

### 总结：

docker+wsl2=轻量化linux虚拟机，可以直接pull相关的环境到docker同时支持GPU加速，同时解决了windows无法跑linux代码的缺陷。

当他人项目里有Dockerfile、docker-compose.yml可以很好部署，当没有的尚不确定是否可以自己编写Dockerfile



