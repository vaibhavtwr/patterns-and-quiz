#!/usr/bin/python
#program to print fibonaci
n=int(input("enter the no. for fibonacci"))
a=0
b=1
for i in range(1,n):
	a,b=b,a+b
	print(a)



