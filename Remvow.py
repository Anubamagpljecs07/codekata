k=input()
s=list(k)
v=['a','A','e','E','i','I','o','O','u','U']
for i in s:
    if i in v:
        s.remove(i)
j=len(s)-1
while j>=0:
    print(s[j],end="")
    j-=1
