#Python Program to Swap Two Variables 
a=int(input("enter first variable"))
b=int(input("enter second value"))
txt="before swapping a={},b={}"
print(txt.format(a,b))
a,b=b,a
txt="after swapping a={},b={}"
print(txt.format(a,b))
