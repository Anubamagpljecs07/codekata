#g anu
n=int(input())
for i in range(0,1000):
    if 2**i==n:
        s="yes"
        break
    else:
        s="no"
print(s)
