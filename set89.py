import math
d,e=map(int,input().split())
v=d*e
root=math.sqrt(v)
if(v==int(root + 0.5) ** 2):
    print("yes")
else:
    print("no")
