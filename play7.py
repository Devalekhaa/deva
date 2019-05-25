o=list(map(str,input()))
g=""
for i in range(0,len(o)-1,2):
    g=o[i]
    o[i]=o[i+1]
    o[i+1]=g
for i in range(0,len(o)):
    print(o[i],end="")
