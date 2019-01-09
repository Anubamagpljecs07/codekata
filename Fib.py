#g anu
a,b,c,d=0,1,0,0
f=[]
n=int(input())
if n!=1:
	while(c<n):
		d=a+b
		a,b=b,d
		c+=1
		f.append(a)
	for i in range(0,len(f)):
		if i==0:
			print(f[i],end="")
		else:
			print("",f[i],end="")
else:
	print(1)
