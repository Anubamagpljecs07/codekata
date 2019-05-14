n,m=map(int,input().split())
s=list(map(int,input().split()))
s=sorted(s,reverse=True)
c=0
for i in s:
	if i<=m:
		d=m//i
		c+=d
		m=m-(d*i)
print(c)
