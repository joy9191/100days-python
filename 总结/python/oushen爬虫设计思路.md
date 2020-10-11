爬取数据、数据存储等设计思路与cnbeta整体相似，不同之处主要有以下几点：
1. 网站有反爬虫机制
网站做了简单的反爬虫机制，请求体中未带浏览器信息会被拦截，直接get请求会被拦截报403，基于这一点，请求时添加User-Agent伪装成浏览器请求，就能访问了。
如何确定网站做了什么样的反爬虫机制？
首先，直接urlopen访问url后调用read函数获取url的响应体，发现报错，这时需要确定是否有http code。我这里用的笨办法抓包，其实可以用getcode()直接查看。但抓包也有个好处可以直接到用爬虫访问和用浏览器访问的区别，直接能看出请求头中缺少浏览器信息，于是随机添加常用浏览器信息到user-agent。
```
my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]
response.add_header('User-Agent', random.choice(my_headers))
```
除了增加header，有些网站还有可能在短时间内直接使用Get获取大量数据，会被服务器认为在对它进行攻击，所以拒绝我们的请求，自动把电脑IP封了，这时可以使用代理ip来解决，这个项目中暂时没遇到这个问题，先记下来后续可以加入实战。
https://app.yinxiang.com/fx/be3a2e0d-112f-416f-8306-4a954dbf8bce

1. 解决爬虫假死问题
在爬取过程中，经常出现卡住假死的问题，程序不往下运行也不报错，由于卡住的地方不一定，初步怀疑是爬虫环境网络问题，也可能是对方网站限流，无论是哪种都必须加入超时机制和异常处理。
1)超时处理
不能让url连接无限制保持连接，这样程序将无法继续，使用urlopen带的参数限制超时时间
`urllib2.urlopen(response, timeout=20)`
这样20s过后如果依然没有返回会返回一个socket timed out报错。
加入超时机制就避免了卡住的问题，下面就是要处理异常了。
2）异常处理
爬取过程中会出现各种问题，比如上述的url访问超时，再比如翻页到n+1页页面不存在报404需要结束程序，还有url访问超时了urlopen的返回一定是None。

```
try：
    r = result.read()
    except urllib2.HTTPError as error:
        logging.error('Data not retrieved because %s\nURL: %s', error, href)
    except urllib2.URLError as error:
        if isinstance(error.reason, socket.timeout):
            logging.error('socket timed out - URL %s', href)
        else:
            logging.error('some other error happened')
    except socket.timeout as error: 
        print 'socket timed out3'
        logging.error('socket timed out - URL %s', href)    
    else:
        ...
```

try except else语法

```
try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生
```
还有其他异常处理方式，可以参考菜鸟教程https://www.runoob.com/python/python-exceptions.html

针对访问超时urlopen返回为None的问题，就比较简单，加入条件判断urlopen返回的对象是否为空来解决。