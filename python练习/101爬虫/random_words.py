#!usr/bin/python
#coding=utf-8

import random

def random_str():
	seed_noun=[u'宝宝',u'土豆',u'传达',u'冬天',u'传达']
	seed_adj=[u'漂亮',u'温暖',u'健全']
	seed_verb=[u'传达',u'检查']
	res=random.choice(seed_words)
	print seed_words
	print res


if __name__ == '__main__':
	random_str()