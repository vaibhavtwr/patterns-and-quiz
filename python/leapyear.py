#!/usr/bin/python
#program to check year is leap year
n=int(input("enter the year"))
if(n%4==0 and n%100==0):
	print("{} is leap year".format(n))
else:
	print("{} is not a leap year".format(n))
