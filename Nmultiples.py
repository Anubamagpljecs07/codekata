n=int(input())
k=0
c=0
if n==0:
        print(0,0,0,0,0)
else:
        for j in range(n,10000000):
                if j%n==0:
                    k=k+1
                    c+=1
                    if c==1:
                        print(j,end="")
                    else:
                        print("",j,end="")
                    if k==5:
                        break
