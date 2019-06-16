import math
d=int(input())
e=math.radians(d)
if d==90:
    print(1)
else:
    print(round(math.sin(e),1))
