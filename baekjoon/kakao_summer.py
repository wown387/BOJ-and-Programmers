
def solution(numbers, hand):
    dic = {}
    k = 1

    for i in range(3):
        for j in range(3):
            dic[k] = (i, j)
            k = k + 1

    dic[0] = (3, 1)
    dic["*"] = (3, 0)
    dic["#"] = (3, 2)

    result = ""

    left = [1, 4, 7]
    right = [3, 6, 9]
    l_position = "*"
    r_position = "#"

    for i in numbers:
        if i in left:
            result = result + "L"
            l_position = i
        elif i in right:
            result = result + "R"
            r_position = i

        else:

            l_far = abs(dic[l_position][0] - dic[i][0]) + abs(abs(dic[l_position][1] - dic[i][1]))

            r_far = abs(dic[r_position][0] - dic[i][0]) + abs(abs(dic[r_position][1] - dic[i][1]))

            if l_far > r_far:
                result = result + "R"
                r_position = i
            elif r_far > l_far:
                result = result + "L"
                l_position = i
            else:
                result = result + hand[0].upper()
                if hand == "left":
                    l_position = i
                else:
                    r_position = i

    print(result)

    return result

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
solution(numbers,hand)