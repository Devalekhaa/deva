a=input()
m=0
for i in range(0,len(a)):
    s=a.count(a[i])
    if s>m:
        m=s 
        d=a[i]
print(d)
