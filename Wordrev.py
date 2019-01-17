s=input()
l=list(s.split(" "))
for i in range(0,len(l)):
	if i==len(l):
		print(l[i][::-1])
	else:
		print(l[i][::-1],end=" ")
