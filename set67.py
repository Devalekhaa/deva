d,e = (input()).split()
d= int(d)
e= int(e)
a= list(map(int,input().split()))
l=a.count(e)
if(l>0):
	print("yes")
else:
	print("no")
