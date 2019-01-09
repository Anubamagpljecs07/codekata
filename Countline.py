#g anu
s=input()
c=0
for i in range(0,len(s)):
    if i==len(s)-1:
        if i!=".":
        	c+=1
    elif s[i]==".":
    	c+=1
print(c)
