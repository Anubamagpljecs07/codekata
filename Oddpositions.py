n=input()
def isodd(x):
    if x%2==1:
        a="O"
    else:
        a="E"
    return a
c=0
for i in range(0,len(n)):
    if isodd(i)=="O":
        c+=1
        if c==1:
            print(n[i],end="")
        else:
            print("",n[i],end="")
