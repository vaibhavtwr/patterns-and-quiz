#!/usr/bin/python
#program to print prime no in given range
n=int(input("enter the range that you want to get prime no."))
print("prime no. are")
for i in range(1,n):
	c=0;
	for j in range(1,i):
		if(i%j==0):
			c=c+1
	if c==1:
		print(i)
