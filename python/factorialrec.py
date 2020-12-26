#!/usr/bin/python
#program to find factorial using recursion
n=int(input("enter no to find factorial"))
def fact(n):
	if n==1:
		return n
	else:
		return n*fact(n-1)
print(fact(n))
