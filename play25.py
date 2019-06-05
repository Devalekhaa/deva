d=int(input())
e=list(map(str,input().split()))
v=sorted(e,key=len)
for i in range(len(v)-1):
    if len(v[i])==len(v[i+1]) and v[i]>v[i+1]:
        v[i],v[i+1]=v[i+1],v[i]
print(*v)
