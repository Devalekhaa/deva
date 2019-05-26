d=input()
count=0
for c in d:
    if (not c.isalnum()):
        count=count+1
print(count)
