v,w=map(int,input().split())
a=v*w
b=[]
for i in range(1,a+1):
    if i%v==0 and i%w==0:
        b.append(i)
print(min(b))
