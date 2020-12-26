#!/usr/bin/python
#program to check prime no.
n=int(input("enter no for check prime no."))
c=0
for i in range(1,n):
	if(n%i==0):
		c=c+1
if(c==1):
	print("{} no is prime no.".format(n))
else:
	print("{} no is not prime no.".format(n))

