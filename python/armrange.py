#!/usr/bin/python
#program for armstrong in range
n=int(input("enter first no."))
n1=int(input("enter second no."))
for i in range(n,n1+1):
	c=len(str(i))
	j=i	
	su=0
	while(j>0):
		rem=j%10
		su=su+rem**c
		j=j/10
	if(su==i):
		print(su)

