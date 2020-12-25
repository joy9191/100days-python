# 1、playwright介绍

`Playwright`是一个强大的Python库，仅用一个API即可自动执行`Chromium`、`Firefox`、`WebKit`等主流浏览器自动化操作，并同时支持以无头模式、有头模式运行。

从安装到第一次录制脚本，给我感觉优点是安装简单快速，脚本录制可靠，功能强大简洁，缺点是新出来的工具，没有api文档，使用教程和相关文档比较少，可以当一当吃螃蟹的人了。

# 2、playwright使用

## 安装

```text
# 安装playwright依赖库，需要python3.7
pip install playwright

# 安装浏览器驱动文件（chromium、firefox、webkit）
python -m playwright install
```

## 录制

使用`Playwright`无需写一行代码，我们只需手动操作浏览器，它会录制我们的操作，然后自动生成代码脚本。

录制命令codegen，打开chrome无头模式开始脚本录制

```text
# 命令行键入
python -m playwright codegen
```

`codegen`的用法可以使用`--help`查看，如果有其他需要可以添加`options`。

```python3
python -m playwright codegen --help
Usage: index codegen [options] [url]

open page and generate code for user actions

Options:
  -o, --output <file name>  saves the generated script to a file
  --target <language>       language to use, one of javascript, python, python-async, csharp (default: "python")
  -h, --help                display help for command

Examples:

  $ codegen
  $ codegen --target=python
  $ -b webkit codegen https://example.com
```

options含义：

- -o：将录制的脚本保存到一个文件

- --target：规定生成脚本的语言，有`JS`和`Python`两种，默认为Python

- -b：指定浏览器驱动，浏览器选项如下（缺省默认为chromium）

  ```undefined
  cr 谷歌浏览器，或全称chromium
  ff 火狐浏览器，或全称firefox
  wk 全称webkit
  ```

例如用chromium打开京东录制操作并存储到my.py文件中，文件存储在执行命令的目录下

```csharp
python -m playwright codegen -o my.py -b https://jd.com
```

## 其他操作

--save-storage与--load-storage是个非常实用的命令

用下面命令访问网站并登陆，关闭浏览器时自动把cookie等浏览器信息存入jd文件中

```cpp
python -m playwright cr https://jd.com --save-storage jd
```

使用时用下述命令直接调用，打开页面即为上次登陆状态

```cpp
python -m playwright cr https://jd.com --load-storage jd
```

假如我有多个网站帐号就可以存在多个不同文件，使用时输入命令即可，文件默认储存在当前执行命令的目录

在网站录制操作的过程中也可以用--save，例如：

```csharp
python -m playwright codegen --target python -o login.py https://jd.com --save-storage jd
```

这样py代码中也生成了保存信息到本地的功能代码，适合于更新帐号信息，然后录制操作只用录制登陆后的页面即可，如下命令，直接读取已登陆的状态，然后就能在已登陆状态下录制：

```csharp
python -m playwright codegen -o run.py https://jd.com --load-storage jd
```

## 执行

很简单，直接执行py文件

```
python run.py
```

### 开源地址

[https://github.com/microsoft/playwright](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fmicrosoft%2Fplaywright)
[https://github.com/microsoft/playwright-python](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fmicrosoft%2Fplaywright-python)

