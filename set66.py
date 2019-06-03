d=input()
l1=l2=0
for i in d:
    if i.isalpha():
        l2+=1
    elif i.isnumeric():
        l1+=1
if l1>=1 and l2>=1:
    print('Yes')
else:
    print('No')
