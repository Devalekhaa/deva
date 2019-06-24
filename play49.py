d=int(input())
if d>=-2**15+1 and d<=2**15+1: 
    print("INT")
elif d>=-2**31+1 and d<=2**31+1: 
    print("LONG INT")
else: 
    print("LONG LONG")
