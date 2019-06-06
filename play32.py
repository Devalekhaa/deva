d,e=map(int,input().split())
v=list(map(int,input().split()))
r=0
for i in range(len(v)):
  if (v[i]==e):
    r+=1
    print("Yes")
    break
else:
  print("No")

