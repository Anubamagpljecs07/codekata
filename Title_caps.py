s=input()
l=list(s.split())
a=""
for i in l:
	for j in range(len(i)):
		if j==0:
			a=a+i[j].upper()
		else:
			a=a+i[j]
	a=a+" "
g=""
for i in range(len(a)-1):
	g=g+a[i]
print(g)
