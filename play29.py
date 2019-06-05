try:
	d,e=map(int,input().split(" "))
	v=0
	for i in range(d,e+1):
		for j in range(1,i+1):
			if j**2==i:
				v+=1
	print(v)
except ValueError:
	print("invalid")
