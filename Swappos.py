s=input()
x=[]
for i in range(0,len(s)):
    if i%2==0:
        x.append(s[i+1])
        x.append(s[i])
    i=i+1
for i in x:
    print(i,end="")
        
