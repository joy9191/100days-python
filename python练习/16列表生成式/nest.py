#!/usr/bin/python
# coding=utf-8

names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 录入五个学生三门课程的成绩
# 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
scores = [[None] * len(courses)] * len(names)
print(scores)
# scores = [[None] * len(courses) for _ in range(len(names))]
# print(scores)
for row, name in enumerate(names):
    for col, course in enumerate(courses):
    	print(row,col)
    	scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
    	print(id(scores[0]))
    	print(id(scores[1]))


# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中