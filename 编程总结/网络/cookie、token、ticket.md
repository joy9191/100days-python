Cookies、token、ticket、session

https://www.cnblogs.com/webcabana/p/7624857.html

研究http请求我们会发现cookies、token、ticket、session

先分别来看看这几个概念

1、Cookie 用于存储 web 页面的用户信息。

由于HTTP是一种无状态的协议，服务器单从网络连接上无从知道客户身份。怎么办呢？就给客户端们颁发一个通行证吧，每人一个，无论谁访问都必须携带自己通行证。这样服务器就能从通行证上确认客户身份了。这就是Cookie的工作原理。
具体来说：
1）客户端A第一次向服务器B发起请求时，服务端判断没有Cookie，生成Cookie
2）服务端在响应中添加Cookie后返回
3）当客户端A再次向服务器B发起请求时，请求报文中带上了Cookie，服务端通过Cookie确定客户端A的身份，并返回相应结果
经常被应用于登录

2、Session是服务器端使用的一种记录客户端状态的机制，使用上比Cookie简单一些，服务器使用一种类似于[散列表](https://baike.baidu.com/item/哈希表/5981869?fr=aladdin&fromid=10027933&fromtitle=散列表)的结构来保存信息。
session的工作原理：
1）在程序运行时服务端就创建Session,保存在服务器中，同时程序会为该Session生成唯一的Session id
2)客户端发送带登录信息（用户名、密码、验证码等）的请求，服务端向客户端发送包含刚生成的Session id的Cookie，并记录认证状态
3）客户端再次发出请求时带上Cookie，服务端通过Cookie中的Session id判断用户身份

3、token
