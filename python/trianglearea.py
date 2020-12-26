#Python Program to Calculate the Area of a Triangle 
import math
a=int(input("enter the first side of triangle"))
b=int(input("enter the second side of triangle"))
c=int (input("enter the third side of triangle"))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)
