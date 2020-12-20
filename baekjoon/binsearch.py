

def bin_search(target,data):
    data.sort()
    start=0
    end=len(data)-1

    while start<=end:
        answer=0
        mid=(start+end)//2
        if data[mid]==target:
            return mid
        elif data[mid]<target:
            start=mid+1
        else:
            end=mid-1

    return None





num=15
a=[1,4,7,11,15,17,20,23,27,30,56,77,79,83,99]

top = len(a)
bottom = 0
count=0
while True:
    mid = (top + bottom) // 2
    if a[mid] > num:
        top = mid

    elif a[mid] < num:
        bottom = mid

    else:
        print(mid,a[mid])
        break

    if top-bottom<2:
        count=count+1
    if count>5:
        print(-1)
        break


def cal(mid,times):
    sum = 0
    for i in times:
        sum = sum + i // mid
    return sum

def cal2(mid,times):
    count = 1
    house = []
    for index, i in enumerate(times):
        if index == 0:
            house.append(i)
        else:
            if house[-1] + mid <= i:
                count = count + 1
                house.append(i)

    return count

def solution(n, times):
    times.sort()
    start =1
    end = max(times)-times[0]
    answer = 0

    while start <= end:

        mid = (start + end) // 2

        a=cal2(mid,times)
        if  a<n:
            end = mid - 1

        else:
            start=mid+1

            if answer < mid:
                answer=mid



    return answer

"""a,n=map(int,input().split())
times=[]
for i in range(a):
    b=int(input())
    times.append(b)"""

n=25
times=[11, 6, 4, 4]
print(solution(n,times))








