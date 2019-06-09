d=int(input())
e=0
for i in range(2,d//2):
    if d%i==0:
        e=1
if e==0:
    print ("no")
else:
    print("yes")
