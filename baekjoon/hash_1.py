
def solution(name, name2):
    dic = {}
    for i in name:
        h = ord(i[0])
        a = dic.get(h)
        if a == None:
            dic[h] = i
        else:
            if type(dic[h]) == list:
                dic[h].append(i)
            else:
                dic[h] = [a]
                dic[h].append(i)

    for i in name2:
        h = ord(i[0])

        if type(dic[h]) == list:
            if len(dic[h])==1:
                del dic[h]
            else:

                di_in = dic[h].index(i)
                del dic[h][di_in]
        else:
            del dic[h]

    answer = list(dic.values())[0]

    if type(answer)==list:

        answer =answer[0]


    print(answer)
    return answer


"""
a=["a","b","a"]
b=["a","a"]
solution(a,b)"""