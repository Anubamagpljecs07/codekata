a,d,n=map(int,input().split())
l=[]
c=1
for i in range(a,1000,d):
	if c<=n:
		l.append(i)
		c+=1
s=sum(l)
print(s)
