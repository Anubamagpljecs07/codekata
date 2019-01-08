n=int(input())
c=0
for j in range(n,10000000):
        if j%n==0:
            c+=1
            print(j,end=" ")
            if c==5:
                break
