#Python Program to Convert Kilometers to Miles 
ch=int(input("enter 1 for change in kilometers to miles \n enter 2 for change in miles to kilometers"))
if (ch==1):
	n=int(input("enter the distance in kilometers"))
	m=0.621371*n
	txt="you distance in kilometer {} and in miles {}"
	print(txt.format(n,m))
elif (ch==2) :
	n=int(input("enter the distance in miles"))
	km=1.60934*n
	txt="your distance in miles {} and in kilometers {}"
	print(txt.format(n,km))
else:
	print("you enter wrong choice")
