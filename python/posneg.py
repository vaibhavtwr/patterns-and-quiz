#!/usr/bin/python
#python program to check no is positive or negative or zero
n=int(input("enter the no for check"))
if(n>0):
	print("{}is positive".format(n))
elif(n<0):
	print("{} is negative".format(n))
else:
	print("no. is 0")
