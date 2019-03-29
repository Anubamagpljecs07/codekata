n,m=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l,reverse=True)
s=0
for i in l:
	while(m!=0):
		s=s+(m%i)
		m=m//i
print(s)
