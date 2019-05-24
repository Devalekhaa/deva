d=int(input())
a=input().split(' ')
v= [int(i) for i in a]
v.sort()
for i in range (d):
    print(v[i],end=" ")
