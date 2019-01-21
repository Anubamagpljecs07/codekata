def isprime(x):
    for i in range(2,x):
        if x%i==0:
            a="yes"
            break
    else:
        a="no"
    return a
n=int(input())
print(isprime(n))
