a=input()
mn=0
for i in range(0,len(a)):
    s1=a.count(a[i])
    if s1>mn:
        mn=s1 
        d=a[i]
print(d)
