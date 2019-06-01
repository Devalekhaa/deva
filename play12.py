import sys, string, math
a,b = map(int,input().split())
b = b%a
v1 = list(map(int,input().split()))
v2 = v1[-b:] + v1[:-b]
print(*v2)
