#G
def gcd(x,y):
	while(y):
		x,y=y,x%y
	return x
n,m=map(int,input().split())
a=n*m
g=gcd(n,m)
x=a//g
print(x)
