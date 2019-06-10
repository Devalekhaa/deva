d=int(input())
e=0
for i in range(d):
	v,a=map(int,input().split())
	if v<a:
		e=e+1
print(e)
