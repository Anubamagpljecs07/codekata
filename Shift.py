n,k=map(int,input().split())
l=list(map(int,input().split()))
a=[]
for j in range(len(l),len(l)-k,-1):
    a.append(l[j-1])
    l.pop()
for i in l:
    a.append(i)
print(a)
