#!/usr/bin/python
# coding=utf-8

# 给定一个正整数，编写程序计算有多少对质数的和等于输入的这个正整数，并输出结果。输入值小于1000

def is_prime(num):
	is_prime=True
	for i in range(2,num-1):
		if num%i==0:
			is_prime=False
			break
		else:
			is_prime=True
	# print(num,is_prime)
	return is_prime

def prime_num(num):
	# num_p=2
	# prime_list=[]
	# while num_p<num:
	# 	# print(num_p)
	# 	if is_prime(num_p):
	# 		prime_list.append(num_p)
	# 	num_p+=1
	prime_list = [i for i in range(2,num) if is_prime(i)]
	print(prime_list)
	print("_______________")
	return prime_list

def main():
	num_i=int(input('请输入一个正整数：'))
	p_count=0
	p_list=prime_num(num_i)
	for a in p_list:
		if num_i-a in p_list and a<num_i-a:
			p_count +=1
	print(p_count)
	x = 'apple'
	print(type(x))

if __name__ == '__main__':
	main()