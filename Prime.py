def isprime(x):
	for i in range(2,x):
		if x%i==0:
			a="no"
			break
	else:
		a="yes"
	return a
n=int(input())
print(isprime(n))
