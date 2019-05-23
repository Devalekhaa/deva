n,a,d=input().split()
n=int(n)
a=int(a)
d=int(d)
sum=0
for i in range(n):
    res=(i*d)+a
    sum=sum+res
print (sum)
