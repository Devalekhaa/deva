d,e=list(map(str,input().split()))
v=0
for i in range(0,len(d)):
    if d[i]!=e[i]:
        v=v+1
if v==1:
    print("yes")
else: print("no")
