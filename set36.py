q=int(input())
a=input()
a=a.split(' ')
e= [int(i) for i in a]
e.sort()
for i in range (q):
    print(e[i],end=" ")
