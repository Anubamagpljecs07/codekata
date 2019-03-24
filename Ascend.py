n=int(input())
l=list(map(int,input().split()))
g=sorted(l)
c=0
for i in range(n):
	for j in range(n):
		if i==j:
			if l[i]!=g[j]:
				print(i)
				c+=1
				break
	if c==1:
		break
