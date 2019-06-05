d=input()
e=''
for i in d:
    if i.isupper():
        e+=i.lower()
    if i.islower():
        e+=i.upper()
print(e)

