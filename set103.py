d=int(input())
e=list(map(int,input().split()))
s=0
t=[]
for i in e:
  t.append(i)
for i in t:
  s=s+i
print(s)
