a=int(input())
t=a
r=0
while(a>0):
    dig=a%10
    r=r*10+dig
    a=a//10
if(t==r):
    print("yes")
else:
    print("no")
    
    
