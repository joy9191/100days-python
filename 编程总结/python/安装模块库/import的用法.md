python中import的用法
import语句用来导入其他python文件（专业术语：模块module），使用该模块里定义的类(class)、方法(def)、变量，从而达到复用代码的目的。
下面来总结下import语句的几种用法
第一种`import module_name`
import后直接接模块名。这种情况下，python会在两个地方寻找这个模块，第一是sys.path（通过运行代码`import sys; print(sys.path)`查看）下，内置模块和自行安装工具包（例如pip安装）的目录一般就在sys.path中，所以这类库可以直接import。第二就是运行文件所在目录的文件，例如a.py和b.py文件都在test目录目录下，示例如下：
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
之前用pip3安装了appium后，`import appium`时报`No module name appium`，是由于安装的路径在`/Library/Python/3.7/site-packages`下，而这个路径没有在sys.path中，所以在其他路径下执行py文件会报错，而在`/Library/Python/3.7/site-packages`路径下直接import appium才不报错，是因为python运行文件所在目录的文件。
用上述方法导入原有的sys.path中的库没有问题。但是，最好不要用上述方法导入同目录下的文件！因为这**可能会出错**。演示这个错误需要用到import语句的第二种写法，所以先来学一学import的第二种写法。
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
这是import第二种写法，`from package_name import module_name`
但如果用上面的写法
```
# a.py
from step import c
    c.printSelf()
```