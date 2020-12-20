import math

def solution(w,h):
    if w==h:

        return h

    sum = 0
    x1 = 0
    y1 = (-h / w) * x1 + h

    n_y1 = math.ceil(y1)

    x2 = 1
    y2 = (-h / w) * x2 + h

    n_y2 = math.floor(y2)

    sum = sum + n_y1 - n_y2


    for i in range(1,w):
        n_y1 = math.ceil(y2)

        x2 = i + 1
        y2 = (-h / w) * x2 + h

        n_y2 = math.floor(y2)

        sum = sum + n_y1 - n_y2

    answer = w * h - sum
    return answer



print(solution(1,2))


def solution(w, h):
    sum = 0
    m = h / w
    i=0
    while  i < w:
        y = m * i
        sum += math.floor(y)
        print(math.floor(y))
        i=i+1
    print(sum * 2)
solution(8,12)

def solution(w,h):
    if w == h:
        answer = w * h - h
        return answer
    if w == 1 or h == 1:
        return 0

    # w, h의 공약수를 저장할 리스트 생성
    temp_w = []
    temp_h = []

    # w와 h는 1억이하 자연수이다.
    if w <= 10000**10000 and h <= 10000**10000:

        # for문을 돌며 공약수를 저장합니다.
        for i in range(w, 0, -1):
            if w%(i)==0: temp_w.append(i)
        for j in range(h, 0, -1):
            if h%(j)==0: temp_h.append(j)
    else: return 0

    # temp_w와 temp_h의 최대공약수가 1일 때 (w * h) - (w + h - 1)을 리턴한다.
    # temp_w와 temp_h의 최대공약수가 1초과일 때 (w * h) - (w + h - 최대공약수))을 리턴한다
    # 교집합을 구하려면 type이 set이어야 한다.
    temp_w_set = set(temp_w)
    temp_h_set = set(temp_h)
    if max(temp_w_set&temp_h_set) == 1: return (w * h) - (w + h - 1)
    elif max(temp_w_set&temp_h_set) > 1: return (w * h) - (w + h - max(temp_w_set&temp_h_set))