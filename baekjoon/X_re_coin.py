import heapq


def cal(a):
    count = 0
    answer = []
    heapq.heapify(answer)
    for i in a: a
    for j in money:
        if i - j >= 0:
            heapq.heappush(answer, i - j)
    if len(answer) == 0:
        return 0
    while answer[0] == 0:
        heapq.heappop(answer)
        count = count + 1

    return answer, count


n=5
money=[2,1]
money.sort()
a=[n]
count=0
for k in range(n//money[0]):
    a,b=cal(a)
    if a==0:
        break
    count=count+b
print(count)







