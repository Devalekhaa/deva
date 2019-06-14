d,e=map(int,input().split())
f=list(map(int,input().split()))
for i in range(1,d+1):
    if i==e:
        print(f[i-1])
