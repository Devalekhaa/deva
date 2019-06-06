import sys,string, math,itertools

def m(s) :
    d = {}
    for c in s :
        if not c.isspace() :
            d[c] = d.get(c,0) + 1
    m = sys.maxsize
    l = []
    m = min(d.values())
    for k,v in d.items() :
        if v == m :
            l.append(k)
    return l

s = input()
n = len(s)
l = m(s)
print(*l)
