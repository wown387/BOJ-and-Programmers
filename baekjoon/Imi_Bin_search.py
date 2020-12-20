n=6
times=[7,10]


start=1
end=max(times)*n

print(start,end)

def cal(mid):
    sum=0
    for i in times:
        sum=sum+mid//i
    return sum

print(cal(15))
answer=end
while start<=end:
    mid=(start+end)//2

    if cal(mid)>=n:
        end=mid-1
        if answer>mid:
            answer=mid
    else:
        start=mid+1

    print(mid)

print(answer)





def cal(mid):
    sum = 0
    for i in times:
        sum = sum + mid // i
    return sum

def solution(n, times):
    start = 1
    end = max(times) * n
    answer = end
    while start <= end:
        mid = (start + end) // 2
        if cal(mid) >= n:
            end = mid - 1
            if answer > mid:
                answer = mid
        else:
            start = mid + 1
    return answer