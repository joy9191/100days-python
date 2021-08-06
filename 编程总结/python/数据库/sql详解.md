我们通常可以将SQL分为三类：DDL（数据定义语言）、DML（数据操作语言）和DCL（数据控制语言）。DDL主要用于创建（create）、删除（drop）、修改（alter）数据库中的对象，比如创建、删除和修改二维表；DML主要负责插入数据（insert）、删除数据（delete）、更新数据（update）和查询（select）；DCL通常用于授予权限（grant）和召回权限（revoke）。


1、数据库编码
推荐使用utf8格式编码，如果将来数据库中用到的字符可能包括类似于Emoji这样的图片字符，也可以将默认字符集设定为utf8mb4（最大4字节的utf-8编码）

```sql
create database `school` default character set utf8mb4;
```

如果要设置MySQL服务启动时默认使用的字符集，可以修改MySQL的配置并添加以下内容

```sql
[mysqld]
character-set-server=utf8
```

2、存储引擎
创建表时，在create命令最后面加上engine=XXX来指定表的存储引擎，MYSQL中存储机制、索引技巧、锁定水平等技术处理以及其他配套功能成为存储引擎，用户可以根据适用场景选择对应引擎。
MySQL 5.5以后的版本默认使用的存储引擎是InnoDB，它正好也就是推荐使用的存储引擎（因为InnoDB更适合互联网应用对高并发、性能以及事务支持等方面的需求）

3、mysql帮助系统
以？开头，输入需要了解的内容，例如
? data type
? varchat
