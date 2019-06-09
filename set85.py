d=input()
n=len(d)
if n%2!=0:
     print(d[:n//2]+"*"+d[n//2+1:])
else:
     print(d[:n//2-1]+"**"+d[n//2+1:])
