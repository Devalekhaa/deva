x=input().split(" ")
b=input().split(" ")
d=int(x[0])
e=int(x[1])
f=int(b[0])
g=int(b[1])
d=(d*60)+e
f=(f*60)+g
if(d>f):
    d=d-f
else:
    d=f-d
z=d/60
y=d%60
print(int(z),end=" ")
print(y)
