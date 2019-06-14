d,e=map(int,input().split())
l=list(map(int,input().split()))
v=[]
for i in l:
    if i%2!=0:
        v.append(i)
print(v[e-1])
