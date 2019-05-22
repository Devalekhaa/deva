start,end=input().split()
a=int(start)
b=int(end)
for i in range(a+1,b):
    if(i%2==0):
        print(i, end=" ")
