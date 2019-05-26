a=int(input())
v=0
b = 1
c= 1
count = 0
if(a==1):
    print("1")
else:
    if a<= 0:
        v=0
    elif a == 1:
        v=0
    else:
        while count < a:
            print(b,end=" ")
            nth = b + c
            b= c
            c = nth
            count += 1
