def isprime(n):
    for i in range(2,n):
        if n%i==0:
            a=0
            break
    else:
        a=1
    return a
k,m=map(int,input().split())
c=0
for i in range(k+1,m):
    g=isprime(i)
    if g==1:
        c+=1
        if c==1:
            print(i,end="")
        else:
            print("",i,end="")
        
