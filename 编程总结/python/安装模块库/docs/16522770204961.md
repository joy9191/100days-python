# 查看python库介绍
1、查看库介绍
> 1）运行python；

> 2）import 库名，例如：import pylab；

> 3）print(help(库名.quiver))，例如：print(help(pylab.quiver))；
> 
-------

2、查看该库下所有函数
> dir(库名)，例如dir(pylab)
> dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。

-------
3、查看库中某个函数的使用帮助：
> help(库名.函数名)，例如：help(pylab.randn) 

-------
做欧神网站爬虫时，需要调用urllib库，urllib是Python提供的一个用于操作URL的模块，我们爬取网页的时候，经常需要用，python2.x中分urllib和urllib2，python3中urllib整合成一个库。我开发时环境使用的



