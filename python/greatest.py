#!/usr/bin/python
#program to find largest no in 3 no.
n1=int(input("enter first no."))
n2=int(input("enter second no."))
n3=int(input("enter third no."))

if(n1>=n2 and n1>=n3):
	print("{} no is greatest".format(n1))
elif(n3>=n2 and n3>=n1):
	print("{} no is greatest".format(n3))
elif(n2>=n1 and n2>=n3):
	print("{} no is greatest".format(n2))

