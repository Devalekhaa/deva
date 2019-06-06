d=int(input())
e=0
for i in range(2,d//2+1):
    if(d%i==0):
        e=e+1
if(e<=0):
    print("yes")
else:
    print("no")

