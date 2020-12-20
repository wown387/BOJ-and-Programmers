"""pepple=[70, 80, 50]
limit=100

def solution(people, limit):
    pepple.sort()
    result=[limit]
    count=0
    answer=1
    for i in pepple:
        if count==2:
            del result[0]
            result.append(limit)
            answer=answer+1
        a=result[-1]-i
        if a >= 0:
            result[-1]=result[-1]-i
            count=count+1

        elif a<0:
            del result[0]
            result.append(limit)
            answer=answer+1

            result[-1]=result[-1]-i
            count=count+1
    print(answer)
    print(result)
    return len(result)
solution(pepple,limit)"""
limit=100
people=[1,2,3,4,5,99]

people.sort()
w=limit
count=0
boat=1
print(people)
for i in range(len(people)):

    if len(people)==0:
        boat=0
        break



    if count==2 or w-people[i] <0:
        boat=boat+1
        w=limit
        count=0

    w = w - people[i]
    count = count + 1

    if i==len(people)-1:
        break


    print(people[i],w,count, boat)

print(boat)

def solution(people, limit):
    people.sort()
    w = limit
    count = 0
    boat = 1
    for i in range(len(people)):
        if len(people) == 0:
            boat = 0
            break
        if count == 2 or w - people[i] < 0:
            boat = boat + 1
            w = limit
            count = 0
        w = w - people[i]
        count = count + 1

        if i == len(people) - 1:
            break
    return boat


def solution(people, limit):
    people.sort()
    count = 0
    cnt1 = 0

    cnt2 = len(people) - 1

    while True:
        a = limit - people[cnt2]

        if people[cnt2] == 0:
            print(count)
            break

        if a >= people[cnt1]:
            people[cnt1] = 0
            people[cnt2] = 0
            count = count + 1
            cnt1 = cnt1 + 1
            cnt2 = cnt2 - 1
        else:
            people[cnt2] = 0
            cnt2 = cnt2 - 1
            count = count + 1
    answer = count
    return answer
