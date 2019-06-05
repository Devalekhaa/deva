d,e=map(int,input().split())
v=[]
for i in range (1,e+1):
    if d%i==0 and e%i==0:
        v.append(i)
print(v[-1])

