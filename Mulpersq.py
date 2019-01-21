n,m=map(int,input().split())
p=n*m
for i in range(0,100000):
    if pow(i,2)==p:
        print("yes")
        break
else:
    print("no")
