def isprime(x):
    for i in range(2,x):
        if x%i==0:
            a='c'
            break
    else:
        a='P'
    return a
n=int(input())
l=[]
for i in range(2,n+1):
    if n%i==0:
        if isprime(i)=="P":
            l.append(i)
l=sorted(l)
for j in range(0,len(l)):
    if j==0:
        print(l[j],end="")
    else:
        print("",l[j],end="")
