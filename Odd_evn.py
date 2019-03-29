s=input()
a=""
g=""
for i in range(len(s)):
	if i%2==0:
		a=a+s[i]
	else:
		g=g+s[i]
print(a,g)
