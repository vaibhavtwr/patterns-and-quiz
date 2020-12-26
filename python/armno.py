#!/usr/bin/python
#program to check armstrong no.
n=int(input("enter no to check no is armstrong or not"))
c=0
rem=0
su=0
j=n
i=n
while(i>0):
	i=i/10
	c=c+1

while(j>0):
	rem=j%10
	su=su+rem**c
	j=j/10

if(su==n):
	print("{} no is armstrong no.".format(su))
else:
	print("{} no is not armstrong no.".format(n))
