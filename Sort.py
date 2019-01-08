n=int(input())
j=list(map(int,input().split()))
g=sorted(j)
for i in range(0,len(g)):
    if i==0:
        print(g[i],end="")
    else:
        print("",g[i],end="")
