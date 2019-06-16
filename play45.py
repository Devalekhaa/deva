d,e=map(int,input().split())
f=(d//2)-1
for i in range(1,f+1):
  if i*f==e:
    print("yes")
    break
  else:
    f-=1
else:
  print("no")
