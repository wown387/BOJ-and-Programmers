location=2

a=[2, 1, 3, 2]

priorities=[1, 1, 9, 1, 1, 1]
location=0
priorities1=[]
for index,i in enumerate(priorities):
    priorities1.append((i,index))

result=[]
while len(priorities1):
    if priorities1[0][0]<max(priorities1)[0]:
        priorities1.append(priorities1[0])
        del priorities1[0]

    else:
        print(priorities1)
        result.append(priorities1[0][1])
        del priorities1[0]
        continue

print(result)
print(result.index(location)+1)

def solution(priorities, location):
    priorities1 = []
    for index, i in enumerate(priorities):
        priorities1.append((i, index))
    result = []
    while len(priorities1):
        if priorities1[0][0] < max(priorities1)[0]:
            priorities1.append(priorities1[0])
            del priorities1[0]

        else:
            print(priorities1)
            result.append(priorities1[0][1])
            del priorities1[0]
            continue
    answer=result.index(location)+1
    return answer



def solution(a, location):
    count=0
    print(a)
    a[location] = str(a[location])

    c = str(a[location])
    while True:

        for i in a:
            if int(a[0]) < int(i):
                a.append(a[0])
                del a[0]
                break
        max = 0

        for i in a:
            if int(max) < int(i):
                max = i



        if max == a[0]:
            count = count + 1
            if type(a[0])==str:
                print(count)
                break
            else:
                print(a)
                del a[0]






solution(a,location)
