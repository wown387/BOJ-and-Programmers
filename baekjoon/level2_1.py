bridge_length=100
weight=100
truck_weights=[10,10,10,10,10,10,10,10,10,10]


def solution(bridge_length, weight, truck_weights):
    ing = []
    ing_weigh = 0
    j=1
    while True:

        i = 0
        # 다리에 있는 시간 추가 후 기간 난 차량 제
        while True:

            if len(ing) == 0:
                break
            ing[i][1] = ing[i][1] + 1
            if ing[i][1] > bridge_length:
                ing_weigh = ing_weigh - ing[i][0]
                del ing[i]
                i = i - 1
            i = i + 1

            if i >= len(ing):
                break

        # 시간 초과 된 차량 제거
        if len(truck_weights) > 0 and ing_weigh + truck_weights[0] <= weight:
            ing.append([truck_weights[0], 1])
            ing_weigh = ing_weigh + truck_weights[0]
            del truck_weights[0]

        if len(ing) == 0:
            answer=j
            break
        j=j+1

    print(answer)
    return answer

solution(bridge_length, weight, truck_weights)