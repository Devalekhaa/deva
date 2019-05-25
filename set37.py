b=input()
d=0
x=len(b)
if (ord (b[0])<57):
    if(ord (b[0])>47 or ord (b[0])==45 or ord (b[0])== 46):
        for i in range (1,x):
            if(ord (b[i])>43 and ord (b[i])<58):
                d=1
            else:
                d=d-1
    else:
        d=d-1
else:
    d=d-1
if (d>0):
    print("yes")
else:
    print("No")

