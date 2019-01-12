#g anu
l=["I","II","III","IV","V","VI","VII","VIII","IX","X"]
n=input()
c=0
for i in n:
    for j in range(0,len(l)):
        if i==l[j]:
            c=c+(j+1)
print(c)
