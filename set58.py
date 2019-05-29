try:
	c=int(input())
	a=list(map(int,input().split()))
	s=0
	for i in range(0,c):
		s=s+a[i]
	print(s//c)
except ValueError:
	print("invalid")

