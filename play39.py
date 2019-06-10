d=int(input())
e=0
for i in range(18):
    if 2**i==d:
        e=1
        break
if e==1:
    print("yes")
else:
    print("no")
