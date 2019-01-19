n=int(input())
a=[]
s=0
while n>0:
    rem=n%10
    a.append(rem)
    n=n//10
for i in a:
    s=s+pow(i,2)
print(s)
