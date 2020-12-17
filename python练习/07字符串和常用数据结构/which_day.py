#!/usr/bin/python

def is_leap_year(year):
	return year % 4 ==0 and year%100!=0 or year%400==0


def which_day(year,month,date):
	total = 0
	days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]
	if is_leap_year(year):
		for i in range(month-1):
			total+=days_of_month[1][i]
	else:
		for i in range(month-1):
			total+=days_of_month[0][i]
	return total+date

if __name__ == '__main__':
	print which_day(2020,3,11)