d=int(input())
e=0
for i in range(2,d):
	if d%i==0:
		e=1
print("yes" if e==1 else "no")
