#g anu
k,n=map(int,input().split())
c=0
for _ in range(k,n+1):
    for i in range(2,_):
        if _%i==0:
            break
    else:
        c=c+1
print(c)
