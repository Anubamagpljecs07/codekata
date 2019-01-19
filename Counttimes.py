s=input()
a=[]
for i in s:
    l=s.count(i)
    a.append(l)
m=max(a)
c=0
for i in s:
    if s.count(i)==m:
        c+=1
        if c==1:
            print(i)
