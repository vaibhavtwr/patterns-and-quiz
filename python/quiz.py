s = str ( input ( ) )
s1 = s[0] + s[len(s)-1]
if int(s) % int(s1) == 0:
	print("True")
else:
	print("False")
"""
Output
121
True 
#121%11=0
Output 2
123
False
#123%13=6
"""
