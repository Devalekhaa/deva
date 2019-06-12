d=input()
e=[]
for i in d:
    if(i.isdigit())==True:
        e.append(i)
print(*e,sep="")
