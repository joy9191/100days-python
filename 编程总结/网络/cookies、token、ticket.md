cookies、token、ticket、session

https://www.cnblogs.com/webcabana/p/7624857.html

研究http请求我们会发现cookies、token、ticket、session

先分别来看看这几个概念

1、Cookie 用于存储 web 页面的用户信息。

由于HTTP是一种无状态的协议，服务器单从网络连接上无从知道客户身份。怎么办呢？就给客户端们颁发一个通行证吧，每人一个，无论谁访问都必须携带自己通行证。这样服务器就能从通行证上确认客户身份了。这就是Cookie的工作原理。

2、Session是服务器端使用的一种记录客户端状态的机制，使用上比Cookie简单一些，服务器使用一种类似于[散列表](https://baike.baidu.com/item/哈希表/5981869?fr=aladdin&fromid=10027933&fromtitle=散列表)的结构来保存信息。

