len,w,h=input().split()
len=int(len)
w=int(w)
h=int(h)
tsa=2*((len*w)+(w*h)+(h*len))
volume=len*w*h
print(tsa,volume)
