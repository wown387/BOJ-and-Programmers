m="acbbcdc"
k="abc"
num=[]
for i in k:
    if len(num)==0:
        n=m.find(i)
        m=m[:n]+"."+m[n+1:]
        num.append(n)
    else:

        n = m[num[-1]:].find(i)
        print(m[num[-1]+1:],-1)
        for index,j in enumerate(m):
            if j==i and index>num[-1]:
                m = m[:index] + "." + m[index + 1:]
                num.append(index)
                break
        print(m)

answer=m.replace(".","")
print(answer)


blocks=[[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]


result2=[]
upfloor=[]
n=1
for i in blocks:
    floor=["."]*n
    if len(floor)==1:
        upfloor=[i[1]]
        result2.extend(upfloor)
    else:
        floor[i[0]]=i[1]
        while True:

            for j in range(len(floor) - 1):
                if type(floor[j]) == int:
                    floor[j + 1] = upfloor[j] - floor[j]
                elif type(floor[j + 1]) == int:
                    floor[j] = upfloor[j] - floor[j + 1]
            print(floor)
            if "." not in floor:
                result2.extend(floor)
                upfloor = floor
                break
    n=n+1
print(result2)

blocks=[[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]
print(len(blocks))
num_blocks=0
for i in range(1,len(blocks)+1):
    num_blocks=num_blocks+i
result=[""]*num_blocks
result2=[]
upfloor=[]
print(result)
n=1
for i in blocks:
    print(i)

    floor=["."]*n

    if len(floor)==1:
        upfloor=[i[1]]
        result2.extend(upfloor)
    else:
        floor[i[0]]=i[1]
        print(floor,upfloor,-3)

        while True:
            for j in range(len(floor) - 1):
                print(floor[j], floor[j + 1], upfloor[j], -4)
                if type(floor[j]) == int:
                    print(floor[j], floor[j + 1], upfloor[j], -5)
                    floor[j + 1] = upfloor[j] - floor[j]
                elif type(floor[j + 1]) == int:
                    print(floor[j], floor[j + 1], upfloor[j], -5)
                    floor[j] = upfloor[j] - floor[j + 1]

            if "." not in floor:
                result2.extend(floor)
                upfloor = floor
                break





    print(floor,upfloor,result2)

    n=n+1


