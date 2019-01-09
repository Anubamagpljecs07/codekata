n=int(input())
l=[]
while n>0:
    r=n%10
    l.append(r)
    n=n//10
for i in range(len(l),0,-1):
    if i==len(l):
        print(l[i-1],end=" ")
    else:
        print("",l[i-1],end="")
