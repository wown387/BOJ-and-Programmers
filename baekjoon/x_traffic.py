import math
def solution(lines):
    logs = []
    for line in lines:
        _, done, time = line.split()
        h, m, s = done.split(':')
        end = (int(h)*60*60 + int(m)*60 + float(s))*1000
        logs.append((end-float(time[:-1])*1000+1, end))

    length = len(logs)
    max_ = 1
    for i in range(length-1):
        cnt = 1
        for j in range(i+1, length):
            if logs[j][1] - logs[i][1] >= 4000:
                break
            if logs[j][0] - logs[i][1] < 1000:
                cnt += 1
        max_ = max(max_, cnt)
    return max_


lines=[
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]




lines=["2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
lines=["2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"]
def cal(lines):
    b = lines.split()[2][:-1]
    a = lines.split()[1].split(":")
    time1 = int(a[0]) * 60 * 60 + int(a[1]) * 60 + float(a[2])
    time = [round(time1 - float(b) + 0.001, 3), round(time1, 3)]
    return time

result=[]
for i in lines:
    print(i)
    time=cal(i)
    result.append(time)
print(result)

answer=0
for i in result:
    num1=0
    num2=0
    num3=0
    num4=0
    for j in result:

        if i[0]>=j[0] and i[0]<=j[1]:
            num1=num1+1
        elif round(i[0]-0.999,3)>=j[0] and round(i[0]-0.999,3)<=j[1]:
            num1=num1+1

        if i[0]>=j[0] and i[1]<=j[1]:
            num2=num2+1
        elif round(i[0]+0.999,3)>=j[0] and round(i[0]+0.999,3)<=j[1]:
            num2=num2+1

        if i[1] >= j[0] and i[1] <= j[1]:
            num3 = num3 + 1
        elif round(i[1] - 0.999,3) >= j[0] and round(i[1] - 0.999,3) <= j[1]:
            num3 = num3 + 1

        if i[1] >= j[0] and i[1] <= j[1]:
            num4 = num4 + 1
        elif round(i[0] + 0.999,3) >= j[0] and round(i[0] + 0.999,3) <= j[1]:
            num4 = num4 + 1



    num_max=max(num1,num2,num3,num4)
    if answer<num_max:
        answer=num_max



print(answer)


def cal(lines):
    b = lines.split()[2][:-1]
    a = lines.split()[1].split(":")
    time1 = int(a[0]) * 60 * 60 + int(a[1]) * 60 + float(a[2])
    time = [round(time1 - float(b) + 0.001, 3), round(time1, 3)]
    return time
def solution(lines):
    result = []

    for i in lines:
        time = cal(i)
        result.append(time)

    answer = 0
    for i in result:
        num1 = 0
        num2 = 0
        num3 = 0
        num4 = 0
        for j in result:
            if i[0] >= j[0] and i[0] <= j[1]:
                num1 = num1 + 1
            elif round(i[0] - 0.999, 3) >= j[0] and round(i[0] - 0.999, 3) <= j[1]:
                num1 = num1 + 1
            if i[0] >= j[0] and i[1] <= j[1]:
                num2 = num2 + 1
            elif round(i[0] + 0.999, 3) >= j[0] and round(i[0] + 0.999, 3) <= j[1]:
                num2 = num2 + 1

            if i[1] >= j[0] and i[1] <= j[1]:
                num3 = num3 + 1
            elif round(i[1] - 0.999, 3) >= j[0] and round(i[1] - 0.999, 3) <= j[1]:
                num3 = num3 + 1

            if i[1] >= j[0] and i[1] <= j[1]:
                num4 = num4 + 1
            elif round(i[0] + 0.999, 3) >= j[0] and round(i[0] + 0.999, 3) <= j[1]:
                num4 = num4 + 1

        num_max = max(num1, num2, num3, num4)
        if answer < num_max:
            answer = num_max

    return answer




"""start=math.floor((start))
end=math.ceil(end)
print(start,end,"start end")"""


lines=["2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

lines=[
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]



result=[]
for line in lines:
    line = line.split()
    print(line)
    time1 = line[1].split(":")
    print(time1)
    time2 = float(line[2][:-1])
    print(time2)
    time1 = int(time1[0]) * 60 * 60 + int(time1[1]) * 60 + float(time1[2])
    print(time1,time1-time2)
    time = [round(time1 - time2 + 0.001,3),  time1 ]
    print(time)
    result.append(time)
print(result)

print(len(result))
answer=0

for i in range(len(result)):
    count1=set()
    count2=set()
    print(result[i][0],result[i][1])
    for index,j in enumerate(result):
        if round(result[i][0],3)>=j[0] and round(result[i][0],3)<=j[1]:
            count1.add(index)
        if round(result[i][0]+ 0.999,3)>=j[0] and round(result[i][0]+ 0.999,3)<=j[1]:
            count1.add(index)
        if round(result[i][1],3)>=j[0] and round(result[i][1],3)<=j[1]:
            count2.add(index)
        if round(result[i][1]+ 0.999,3)>=j[0] and round(result[i][1]+ 0.999,3)<=j[1]:
            count2.add(index)
    print(list(count1))
    print(list(count2))
    count=max(len(count1),len(count2))
    if answer<count:
        answer=count
print(answer)


def solution(lines):
    result = []
    for line in lines:
        line = line.split()
        time1 = line[1].split(":")
        time2 = float(line[2][:-1])
        time1 = int(time1[0]) * 60 * 60 + int(time1[1]) * 60 + float(time1[2])
        time = [round(time1 - time2 + 0.001, 3), time1]
        result.append(time)
    answer = 0
    for i in range(len(result)):
        count1 = set()
        count2 = set()
        count3 = set()
        count4 = set()
        for index, j in enumerate(result):
            if result[i][0] >= j[0] and result[i][0] <= j[1]:
                count1.add(index)
            if round(result[i][0] + 0.999, 3) >= j[0] and round(result[i][0] + 0.999, 3) <= j[1]:
                count1.add(index)
            if result[i][1] >= j[0] and result[i][1]<= j[1]:
                count2.add(index)
            if round(result[i][1] + 0.999, 3) >= j[0] and round(result[i][1] + 0.999, 3) <= j[1]:
                count2.add(index)
            if result[i][0] >= j[0] and result[i][0] <= j[1]:
                count3.add(index)
            if round(result[i][0] - 0.999, 3) >= j[0] and round(result[i][0] - 0.999, 3) <= j[1]:
                count3.add(index)
            if result[i][1] >= j[0] and result[i][1]<= j[1]:
                count4.add(index)
            if round(result[i][1] - 0.999, 3) >= j[0] and round(result[i][1] - 0.999, 3) <= j[1]:
                count4.add(index)

        count = max(len(count1), len(count2),len(count3),len(count4))
        if answer < count:
            answer = count
    print(answer)
    return answer



def solution(line):
    if len(line)==1:
        return 1
    result = []
    for time in line:
        time = time.split()

        time1 = time[1].split(":")

        m_s = float(time[-1][:-1])

        sum = int(time1[0]) * 60 * 60 + int(time1[1]) * 60 + float(time1[2])

        sum2 = sum - m_s+0.001
        if sum2<0:
            sum2=0
        print(int(sum2 * 1000), int(sum * 1000))
        result.append((int(sum2 * 1000), int(sum * 1000)))

    print(result)

    start = result[0][0]
    end = result[0][1]
    for i in result:
        if i[0] < start:
            start = i[0]
        if i[1] > end:
            end = i[1]

    print(start, end, -1)
    max = 0
    for i in range(start, end):

        answer = set()
        for j in result:
            if i >= j[0] and i <= j[1] or i + 999 >= j[0] and i + 999 <= j[1]:
                answer.add(j)


        if len(answer) > max:
            max = len(answer)
            print(answer,i)

    print(max)

    return max

