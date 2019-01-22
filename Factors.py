n=int(input())
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
for j in range(0,len(l)):
    if j==0:
        print(l[j],end="")
    else:
        print("",l[j],end="")
