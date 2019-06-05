d,e=map(int,input().split())
input()
v=list(map(int,input().split()))
a=list(map(int,input().split()))
l=[]
for i in range(len(a)):
	v.append(a[i])
	e=max(v)
	l.append(e)
print(*l)
