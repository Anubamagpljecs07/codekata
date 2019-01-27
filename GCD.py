n,m=map(int,input().split())
l=[]
for i in range(1,max(n,m)):
    if n%i==0 and m%i==0:
        l.append(i)
ma=max(l)
print(ma)
