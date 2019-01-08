n=int(input())
n1=n
rev=0
while n>1:
	rem=n%10
	rev=rev*10+rem
	n=n//10
if n==n1:
	print("yes")
else:
	print("no")
