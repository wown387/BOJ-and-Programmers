
b=[1,1,3,3,0,1,1]
a=[]

for i in b:
    if len(a)==0:
        a.append(i)
    else:
        if a[-1]==i:
            continue
        else:
            a.append(i)
print(a)