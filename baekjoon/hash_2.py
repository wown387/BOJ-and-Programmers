par=["mislav", "stanko", "mislav", "ana"]

com=["stanko", "ana", "mislav"]

def solution(participant, completion):
    dic_com = {}
    answer = ""
    for i in com:
        a = dic_com.get(i)
        if a == None:
            dic_com[i] = 1
        else:
            dic_com[i] = dic_com[i] + 1
    for i in par:
        a = dic_com.get(i)
        if a == None or a == 0:
            answer = i
            print(answer)
            break
        else:
            dic_com[i] = dic_com[i] - 1


    return answer



