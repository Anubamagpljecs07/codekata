n=int(input())
l=[]
while n>0:
    r=n%10
    l.append(r)
    n=n//10
for i in range(0,len(l)):
    if i==0:
        print(l[i],end="")
    else:
        print("",l[i],end="")
        
    
    
