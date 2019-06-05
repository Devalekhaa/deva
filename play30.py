d1,d2,e=input().split()
d1=str(d1)
d2=str(d2)
e=int(e)
count=0
for i in range(0,len(d1)):
	if(d1[i]!=d2[i]):
		count+=1
	else:
		continue
if(count==e):
	print("yes")
else:
	print("no")
