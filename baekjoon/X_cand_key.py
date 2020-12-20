
from itertools import combinations
relation=[["100","ryan","music","2"],["200","apeach","math","2"],
          ["300","tube","computer","3"],["400","con","computer","4"],
          ["500","muzi","music","3"],["600","apeach","music","2"]]

n=2
n=1
answer = []
while True:
    item = [i for i in range(len(relation[0]))]
    n_list = list(combinations(item, n))

    can_key = set()
    for i in n_list:
        result = set()
        for j in range(len(relation)):
            key = ""
            for k in i:
                key = key + relation[j][k]
            result.add(key)
        if len(result) == len(relation):
            can_key.add(i)

    can_key = list(can_key)

    for i in can_key:
        answer.append(i)




    if n==len(relation[0]):
        break
    n = n + 1
print(answer)



def solution(relation):
    n = 1
    answer = 0
    while True:

        item = [i for i in range(len(relation[0]))]
        n_list = list(combinations(item, n))

        can_key = set()
        for i in n_list:
            result = set()
            for j in range(len(relation)):
                key = ""
                for k in i:
                    key = key + relation[j][k]
                result.add(key)
            if len(result) == len(relation):
                can_key.add(i)

        can_key = list(can_key)
        answer = answer + len(can_key)

        # 제거
        del_list = set()
        for i in can_key:
            for j in range(n):
                del_list.add(i[j])

        for i in range(len(relation)):

            for j in del_list:
                relation[i][j] = ""


        count = 0
        for i in relation[0]:
            if i != "":
                count = count + 1

        if count < n + 1:
            break

        n = n + 1

    return answer