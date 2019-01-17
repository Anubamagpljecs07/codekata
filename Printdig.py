n=input()
c=[]
for i in n:
	if i.isdigit():
		c.append(i)
for j in range(0,len(c)):
	if j==len(c)-1:
		print(c[j])
	else:
		print(c[j],end="")
