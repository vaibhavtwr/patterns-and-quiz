#!/usr/bin/python
#python program to find the factor of no.
n=int(input("enter the no. for find factorial"))
for i in range(1,n+1):
	if(n%i==0):
		print(i)

