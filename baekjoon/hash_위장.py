clothes=[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

def solution(clothes):
    clo = {}
    for i in clothes:


        if clo.get(i[1]) == None:
            clo[i[1]] = [i[0]]
        else:
            clo[i[1]].append(i[0])

    a = list(clo.keys())

    result = []
    sum = 0
    for j in a:

        sum = sum + len(clo[j])
        result.append(len(clo[j]))
    sum2 = 1

    if len(result) > 0:
        for i in result:
            sum2 = sum2 * (i+1)
        answer = sum2-1
    else:
        answer=0
    print(answer)
    return answer

solution(clothes)