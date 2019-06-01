d=['A','E','I','O','U','a','e','i','o','u']
e=int(input())
v=list(input())
o=[]
for i in range(0,len(v)):
    if v[i] in d:
        continue
    else: o.append(v[i])
for i in range(len(o)-1,-1,-1):
    print(o[i],end="")
