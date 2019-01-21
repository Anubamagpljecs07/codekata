s=input()
l=list(s)
x=len(l)//2
if len(l)%2!=0:
    for i in range(0,len(l)):
        if i==x:
            l[i]="*"
else:
    for i in range(0,len(l)):
        if i==x:
            l[i-1],l[i]="*","*"
for i in l:
    print(i,end="")
        
    
