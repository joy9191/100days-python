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

4、DQL数据库查询语言
1)模糊匹配
-- 在SQL中通配符%可以匹配零个或任意多个字符
select stu_name, stu_sex from tb_student where stu_name like '杨%';

-- 查询姓“杨”名字两个字的学生姓名和性别(模糊)
-- 在SQL中通配符_可以刚刚好匹配一个字符
select stu_name, stu_sex from tb_student where stu_name like '杨_';

-- 查询姓“杨”名字三个字的学生姓名和性别(模糊)，用两个通配符_来匹配
select stu_name, stu_sex from tb_student where stu_name like '杨__';

-- 查询名字中有“不”字或“嫣”字的学生的姓名(模糊)
-- 提示：**前面带%的模糊查询性能基本上都是非常糟糕的**
select stu_name from tb_student 
where stu_name like '%不%' or stu_name like '%嫣%';

2）聚合函数
如果做计数操作，建议使用count(*)，这样才不会漏掉空值

select sum(score) / count(score) from tb_record;
select sum(score) / count(*) from tb_record;

3)分组
-- 查询平均成绩大于等于90分的学生的学号和平均成绩
-- 分组以前的数据筛选使用where子句，分组以后的数据筛选使用having子句
select 
	sid as 学号, 
    round(avg(score),1) as 平均分 
from tb_record 
group by sid having 平均分>=90;

4)子查询
-- 查询年龄最大的学生的姓名(子查询)
-- 嵌套查询：把一个查询的结果作为另外一个查询的一部分来使用。
select stu_name from tb_student where stu_birth=(
	select min(stu_birth) from tb_student
);

5）连接查询
inner join


MySQL中支持多种类型的运算符，包括：算术运算符（+、-、*、/、%）、比较运算符（=、<>、<=>、<、<=、>、>=、BETWEEN...AND...、IN、IS NULL、IS NOT NULL、LIKE、RLIKE、REGEXP）、逻辑运算符（NOT、AND、OR、XOR）和位运算符（&、|、^、~、>>、<<），我们可以在DML中使用这些运算符处理数据。

在查询数据时，可以在SELECT语句及其子句（如WHERE子句、ORDER BY子句、HAVING子句等）中使用函数，这些函数包括字符串函数、数值函数、时间日期函数、流程函数等，如下面的表格所示。

5、索引
索引是关系型数据库中用来提升查询性能最为重要的手段。
* 最适合索引的列是出现在WHERE子句和连接子句中的列。
* 索引列的基数越大（取值多重复值少），索引的效果就越好。
* 使用前缀索引可以减少索引占用的空间，内存中可以缓存更多的索引。
* 索引不是越多越好，虽然索引加速了读操作（查询），但是写操作（增、删、改）都会变得更慢，因为数据的变化会导致索引的更新，就如同书籍章节的增删需要更新目录一样。
* 使用InnoDB存储引擎时，表的普通索引都会保存主键的值，所以主键要尽可能选择较短的数据类型，这样可以有效的减少索引占用的空间，利用提升索引的缓存效果。
