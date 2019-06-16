d=int(input())
e=input().split()
v=[]
for i in sorted(e):
  v.append(i)
if(v==e):
  print("yes")
else:
  print("no")
