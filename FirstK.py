r,s=map(str,input().split())
for i in range(0,int(s)):
    if i==int(s)-1:
        print(r[i])
    else:
        print(r[i],end="")
