# python中import的用法
## import语句的作用
import语句用来导入其他python文件（专业术语：模块module），使用该模块里定义的类(class)、方法(def)、变量，从而达到复用代码的目的。

下面基于python3来总结下import语句的几种用法
## 导入的写法
### 1.`import module_name`
这种写法只能导入package或module,并且使用内部函数或者类的时侯也要加上package或module name的前缀。
import后直接接模块名。这种情况下，python会在两个地方寻找这个模块
1. sys.path（通过运行代码`import sys; print(sys.path)`查看）下，内置模块和自行安装工具包（例如pip安装）的目录一般就在sys.path中，所以这类库可以直接import;
2. 运行文件所在目录的文件，例如a.py和b.py文件都在test目录目录下，示例如下：

```
test/
    a.py
    b.py
```

```
# a.py
import os
import b
b.printSelf()
```

```
# b.py
def printSelf():
    print('In b')
```
此时在test目录下，运行`python a.py`命令，正常运行且打印出`In b`，说明上述写法没问题。
**实战分析**
之前用pip3安装了appium后，`import appium`时报`No module name appium`，是由于安装的路径在`/Library/Python/3.7/site-packages`下，而这个路径没有在sys.path中，所以在其他路径下执行py文件会报错，而在`/Library/Python/3.7/site-packages`路径下直接import appium才不报错，是因为python运行文件所在目录的文件。
**解决办法**
* 使用python -m（后面分析）
```python3 -m pip install some-package```

* 【简单粗暴法】由上面学到的知识可以得出一个方法，将第三方库的安装路径加在sys.path下

```
//将这段代码加到python文件最上方
import sys
sys.path.append(r'实际路径')
```
用上述方法导入原有的sys.path中的库没有问题。但是，最好不要用上述方法导入同目录下的文件！因为这**可能会出错**。演示这个错误需要用到import语句的第二种写法，所以先来学一学import的第二种写法。
### 2.`from package_name import module_name`
在test目录下新建目录step，在step中新建文件c.py
```
test/
    step/
        c.py
    a.py
    b.py
```

```
# c.py
def printSelf():
    print('In c')
```
a中怎样引入c.py模块呢

```
# a.py
from step import c

c.printSelf()
```
It's Ok!
如果用第一种写法导入同目录下的文件有可能会产生问题，下面用一个例子来说明：

在step目录下新建文件d.py
```
test/
    step/
        c.py
        d.py
    a.py
    b.py
```
```
# d.py
def printSelf():
    print('In d')
```
c.py修改一下，文件中直接导入d
```
# c.py
import d
def printSelf():
    print('In c')
```
再运行a.py时，会报d模块不存在。分析下报错原因，a里面`from step import c`导入c，然后在c.py中`import d`导入d模块，a.py与d.py在不同目录下，所以c导入d时报错。
而上面的错误在python2中就不会报错，这里就涉及到import的核心知识点相对导入和绝对导入，**上面两种写法在python2是相对导入，而在python3中是绝对导入。**
## 绝对导入和相对导入
绝对导入和相对导入的关键区别在于，绝对导入能直接import运行文件所在目录下的包或模块。在python3下是绝对导入，基于这一点，导入自己写的文件，如果是非运行入口文件，则需要相对导入。如上述的c.py是非运行入口文件，而a.py是运行入口文件，可以使用绝对导入。
```
#c.py
from . import d
def printSelf():
	print('In c')
```
这样再运行a.py就没毛病了
列举一下相对导入的写法：
```
from . import module_name。导入和自己同目录下的模块。
from .package_name import module_name。导入和自己同目录的包的模块。
from .. import module_name。导入上级目录的模块。
from ..package_name import module_name。导入位于上级目录下的包的模块。
```
当然还可以有更多的.，每多一个点就多往上一层目录。
上面说到“运行入口文件，可以使用绝对导入”，那我偏不，就要用相对导入，可不可以呢，比如写成下面这样：
```
#a.py
from .step import c
c.printSelf()
```
可以是可以，但。。不能用`python a.py`命令，而需要`python -m test.a`
python -m中-m指令是为了让Python预先import你要的package或module给你，然后再执行script。

## import的其他常用方法
### 1. import moudle_name as alias。
有些module_name比较长，之后写它时较为麻烦，或者module_name会出现名字冲突，可以用as来给它改名，如import numpy as np。
### 2. from module_name import function_name, variable_name, class_name。
上面导入的都是整个模块，有时候我们只想使用模块中的某些函数、某些变量、某些类，用这种写法就可以了。使用逗号可以导入模块中的多个元素。
有时候导入的元素很多，可以使用反斜杠来换行，官方推荐使用括号。
### 3. from Tkinter import Tk, Frame, Button, Entry, Canvas, Text, \
```
    LEFT, DISABLED, NORMAL, RIDGE, END	# 反斜杠换行
from Tkinter import (Tk, Frame, Button, Entry, Canvas, Text,
    LEFT, DISABLED, NORMAL, RIDGE, END)	# 括号换行（推荐）
```