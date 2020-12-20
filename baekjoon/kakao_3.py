def solution(n, stage):
    dic = []
    for i in range(1, n + 1):
        sup = 0
        clear = 0
        for j in stage:
            if j >= i:
                sup = sup + 1
            if j > i:
                clear = clear + 1
        if sup==0:
            dic.append((1,i))
        else:
            dic.append((clear / sup, i))

    dic.sort()
    print(dic)
    result = []

    for i in dic:
        result.append(i[1])

    answer = result
    print(answer)
    return answer

stage=[4,4,4,4,4]
n=4
solution(n,stage)