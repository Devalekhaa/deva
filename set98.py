d=input().split()
d=list(map(int,d))
e=d[0]
f=d[1]
if(e>f):
    min1=e
else:
    min1=f
while(1):
    if(min1%e==0 and min1%f==0):
        print(min1)
        break
    min1=min1+1
