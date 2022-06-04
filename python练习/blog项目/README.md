# 100days-python
100天学python


1.首先创建的"blog项目"
2.里层的/blog项目/blog/目录包含这个项目，是个纯python包，如果修改会影响很多引用它的地方出错
```buildoutcfg
|-- blog
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
`-- manage.py
```
3./blog项目/blog/blogs目录是创建的应用


后面我又基于/blog项目/blog/创建了一个项目，叫blog，在/blog项目/blog/blog中创建了名为blogs的应用