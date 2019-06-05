def collinear(a1, b1, a2, b2, a3, b3): 
    if ((b3 - b2)*(a2 - a1) == (b2 - b1)*(a3 - a2)): 
        print("yes")
    else:
        print("no")
a1,b1 = map(int,input().split())
a2,b2 = map(int,input().split())
a3,b3 = map(int,input().split())

collinear(a1, b1, a2, b2, a3, b3)
