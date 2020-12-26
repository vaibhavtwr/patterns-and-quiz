#!/usr/bin/python
ch=int(input("enter the choice \n1 for celsius to fahrenheit\n 2 for fahrenheit to celsius"))
if(ch==1):
	n=int(input("\nenter the temperature in celsius\n"))
	c=(n*9/5)+32
	print("\n{} celsius={} fahrenheit".format(n,c))
elif(ch==2):
	n=int(input("\nenter the temperature in fahrenheit\n"))
	c=(n-32)*5/9	
	print("\n{} fahrenheit={} celsius".format(n,c))


