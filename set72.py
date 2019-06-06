d=input("")
e=0
for i in range(len(d)):
  if(d[i]!="0" and d[i]!="1" ):
    e=e+1
if(e>=1):
  print("no")
elif(e==0):
  print("yes")      
    
 
