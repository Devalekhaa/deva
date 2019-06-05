d,r=map(int,input().split())
e=0
for i in range(d,v+1):
  a=2
  while a<=v:
    if i==a*a:
       e=e+1 
       break
    a+=1
print(e)

