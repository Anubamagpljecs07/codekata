def isarms(n):
    r=0
    while n>0:
        rem=n%10
        r=r+pow(rem,3)
        n=n//10
    return  r
n,m=map(int,input().split())
c=0
for i in range(n+1,m):
    j=i
    g=isarms(i)
    if g==j:
        c+=1
        if c==1:
            print(i,end="")
        else:
            print("",i,end="")
