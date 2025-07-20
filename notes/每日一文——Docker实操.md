# 每日一文——Docker实操

***编辑于2025-7-20***

本篇主要从实操上解决VScode远程连接进入docker容器内部环境，实现本地调试和开发的功能，因为是个人笔记，因此会记录相应的坑以及实操的有效解决办法。

在这篇文章中作者提到了远程连接的两种方法https://blog.csdn.net/qq_19716143/article/details/132310200本文将按照作者提出的两种方法实际操作看看能否顺利运行代码

### 方法一：使用ssh服务远程连接容器

核心是通过在容器内部下载ssh，然后vscode里面的remote ssh插件编写config文件用端口进行连接，类似于ssh远程连接另一个操作系统。但是总是显示报错

```
过程试图写入的管道不存在。
```

这个方法没有成功过。多项排查后可能的原因是端口占用，个人感觉太繁琐了，总之新手不推荐，需要对ssh有一定了解，大概知道什么报错去找什么原因才行。

### 方法二：使用dev-container（新手推荐）

先说说失败经验，官方给的代码文件里有一个code，起初我的思路是如何在code里使用docker的解释器环境，然后尝试了自己写devcontainer文件，但是这样是部分挂载，虽然可以用docker解释器环境了，但是挂载的环境缺少了很多文件，然后导致不停地报错文件路径找不到地问题，总之踩了大坑。

ps：在没有一点基础专业知识以前不要盲信AI，AI给出的方案是片面的，导致你根本不知道解决的逻辑以及你现在究竟处在什么位置，所以无从辨别真伪，只能是不停报错不停换解决方法，这样毫无效率。

推荐对于领域完全未知的时候去看别人的经验贴，一个是这是经过实测的有效方法，可以少走弯路，另一个是相对而言逻辑性更强是否是相同问题看一下帖子就大概知道了。

后来找到一篇https://zhuanlan.zhihu.com/p/530413695作者仅仅用两个图就解释清楚了在VScode里用devcontainer实现远程连接docker的操作。

> 更正：拓展包换版本了
>
> ![image-20250720150741296](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/image-20250720150741296.png)
>
> 下载好以后，在docker后台运行的条件下，找到VS左侧下方容器管理中已经启动的docker环境（补充：一个项目可能会有多个独立的容器，但是只能选择一个容器作为挂载，根据需要去选择）
>
> ![image-20250720150905587](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/image-20250720150905587.png)
>
> ![img](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/v2-82215ed47f9c8ef1ccc33fb564309c97_r.jpg)
>
> 直接搬运的大大原图，已经很详细了。

### 个人说明

在已经运行的docker镜像上attach VScode，相当于容器内置VScode，此时可以理解为打开了一个虚拟机，环境就是docker，因此open folder实则是步入了docker容器内部文件，找到项目代码文件夹打开，然后等待解释器加载，就可以完全实现本地调试开发。

如果说从失败当中学到了什么也许就是docker环境也可以继续配置新库以及增加文件（本质类似虚拟机，具体技术还要深入学习）

加油吧！鹿小葵！*★,°*:.☆(￣▽￣)/$:*.°★* 。

------

### 总结踩坑过程中积累的细小知识点

> ###### 进入容器内部指令+查看docker系统

docker-app里可以直接打开已经激活的docker内部（右键三点）

![image-20250720153246809](https://raw.githubusercontent.com/Arvery/pic-bed/main/img/image-20250720153246809.png)

```
cat /etc/os-release
# 或者更详细一点：
uname -a
```

或者win+r回车进入命令行后

```
docker exec -it dev-kaiwudrl-1 bash  #进入docker内部
cat /etc/os-release
# 或者更详细一点：
uname -a
```

```
docker exec -it <已经运行的docker名字> cat /etc/os-release  #不会进入docker的bash，返回依然在win的cmd内
```

在确认了操作系统后就可以按照相关操作系统的命令行进行操作。

