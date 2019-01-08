n,m=(map(int,input().split()))
c=0
for i in range(n+1,m):
    if i%2==1:
        c+=1
        if c==1:
            print(i,end="")
        else:
            print("",i,end="")
        
