
def solution(strings, n):

    answer = []

    dic = {}
    for i in strings:
        if dic.get(ord(i[n])) == None:
            dic[ord(i[n])] = i
        else:

            if type(dic[ord(i[n])]) == list:
                dic[ord(i[n])].append(i)
                dic[ord(i[n])].sort()


            else:
                a = dic.get(ord(i[n]))
                dic[ord(i[n])] = [a]
                dic[ord(i[n])].append(i)
                dic[ord(i[n])].sort()

    print(dic)

    dic_list = list(dic.keys())
    dic_list.sort()

    print(dic_list)

    for i in dic_list:
        if type(dic[i]) == list:
            for j in dic[i]:
                answer.append(j)

        else:
            answer.append(dic[i])

    print(answer)


    return answer