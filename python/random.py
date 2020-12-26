#Python Program to Generate a Random Number 
import random
n=int(input("enter the size of array"))
arr=[]
for i in range(0,n):
	val=int(input())
	arr.append(val)
print(arr)
b=random.choice(arr)
txt="random no in array is {}"
print(txt.format(b))
a=random.randrange(0,10)
txt1="random no is range 0 to 10 is {}"
print(txt1.format(a))
txt2="random float no. in 0.0 to 0.9 :{}"
c=random.random()

print(txt2.format(c))
