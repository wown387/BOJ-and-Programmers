



def solution(num):

    dic = {1: 1, 2: 2, 3: 4}

    answer = ""

    n = 1

    result = []
    while True:
        count = 0

        for i in range(3):
            num = num - n
            count = count + 1
            if num % (n * 3) == 0:
                result.append(count)
                break
        n = n * 3

        if num == 0:
            break

    for i in reversed(result):
        answer = answer + str(dic[i])
    print(answer)

    return int(answer)

solution(1)