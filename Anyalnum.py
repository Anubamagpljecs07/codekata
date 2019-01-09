s=input()
c=0
d=0
for i in s:
    if i.isalpha():
        c+=1
    elif i.isdigit():
        d+=1
if c>0:
    print("Yes")
else:
    print("No")
    
