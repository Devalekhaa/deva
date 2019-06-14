d=int(input())
e=list(map(int,input().split()))
f=e[:]
f.sort()
for i in range(0,len(e)):
    if e[i] != f[i]:
        print(i)
        break
