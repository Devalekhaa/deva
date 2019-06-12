def hcf(x,y): 
    if(y==0): 
        return x 
    else: 
        return hcf(y,x%y) 
z=list(map(int,input().split()))
print (hcf(z[1],z[0]))
