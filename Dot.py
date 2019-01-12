s=input()
l=list(s)
for i in range(0,len(s)):
	if i==len(s)-1:
		l.append(".")
for i in l:
	print(i,end="")	
