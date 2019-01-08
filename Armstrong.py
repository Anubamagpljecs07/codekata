n=int(input())
n1=n
r=0
while n>0:
    rem=n%10
    r=r+pow(rem,3)
    n=n//10
if r==n1:
    print("yes")
else:
    print("no")
    
