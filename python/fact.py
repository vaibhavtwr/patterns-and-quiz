#!/usr/bin/python
#program to find factorial
n=int(input("enter the no you want to find factorial"))
def fac(n):
	a=1
	for i in range (1,n+1):
		a=a*i
	return a
print(fac(n))
