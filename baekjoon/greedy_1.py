
n=3
lost=[1,2,3]
reserve= [1,2,3]



def solution(n, lost, reserve):
    for j in range(1,n+1):
        if j in lost and j in reserve:
            a=lost.index(j)
            del lost[a]
            b=reserve.index(j)
            del reserve[b]


    for i in range(1, n + 1):
        if i in lost and i - 1 in reserve:
            a = lost.index(i)
            del lost[a]
            b = reserve.index(i - 1)
            del reserve[b]
        elif i in lost and i + 1 in reserve:
            a = lost.index(i)
            del lost[a]
            b = reserve.index(i + 1)
            del reserve[b]

    print(lost,reserve)
    answer = n-len(lost)
    return answer
solution(n,lost,reserve)