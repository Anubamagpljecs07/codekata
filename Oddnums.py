n=input()
def isodd(x):
    if int(x)%2==1:
        a="O"
    else:
        a="E"
    return a
c=0
for i in n:
    if isodd(i)=="O":
        c+=1
        if c==1:
            print(i,end="")
        else:
            print("",i,end="")
