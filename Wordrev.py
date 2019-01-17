#g anu
s=input()
l=list(s.split(" "))
for i in range(0,len(l)):
	if i==0:
		print(l[i][::-1],end="")
	else:
		print("",l[i][::-1],end="")
