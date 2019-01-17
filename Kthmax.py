n,k=map(int,input().split())
l=list(map(int,input().split()))
a=sorted(l)
for i in range(1,k):
	a.pop()
c=max(a)
print(c)
