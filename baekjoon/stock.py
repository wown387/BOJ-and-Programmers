price=[1, 2, 3, 2, 3]


def solution(price):
    result = []

    for i in range(len(price)):
        print(i)
        sum = 0
        for j in range(i + 1, len(price)):
            print(price[i], price[j])
            if price[j] >= price[i]:
                sum = sum + 1
            else:
                sum=sum+1
                break
        print("기간", sum)
        result.append(sum)

    print(result)
    answer = result
    return answer


solution(price)