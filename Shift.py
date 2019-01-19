n,k=map(int,input().split())
l=list(map(int,input().split()))
a=[]
for j in range(len(l),len(l)-k,-1):
    a.append(l[j-1])
    l.pop()
for i in l:
    a.append(i)
for k in range(0,len(a)):
    if k==0:
        print(a[k],end="")
    else:
        print("",a[k],end="")
