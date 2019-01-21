s=input()
l=["a","A","e","E","i","I","o","O","u","U"]
for i in s:
    if i in l:
        print("yes")
        break
else:
    print("no")
