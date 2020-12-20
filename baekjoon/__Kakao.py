
new_id="abcdefghijklmn.p"
import collections
from itertools import combinations

def solution1(new_id):
    new_id = new_id.lower()
    # 1단계

    new_id = list(new_id)
    de_li = "-_."
    for i in range(len(new_id)):
        if new_id[i].isalpha() or new_id[i].isdigit() or new_id[i] in de_li:
            pass
        else:
            new_id[i] = ""
    new_id = "".join(new_id)

    del_li = []
    result = ""
    for i in new_id:
        if i == "." and len(del_li) == 0:
            del_li.append(1)
            result = result + i
        elif i == "." and len(del_li) > 0:
            pass

        else:
            result = result + i
            del_li = []

    new_id = result

    if len(new_id) > 0 and new_id[0] == ".":
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == ".":
        new_id = new_id[:-1]
    if len(new_id) == 0:
        new_id = new_id + "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if len(new_id) > 0 and new_id[-1] == ".":
            new_id = new_id[:-1]
    if len(new_id) < 3:
        while True:
            new_id = new_id + new_id[-1]
            if len(new_id) >= 3:
                break
    answer = new_id
    return answer


def solution2(orders, course):
    result = collections.Counter()

    for i in orders:
        result = result + collections.Counter(i)

    result = result.items()
    result = sorted(result, key=lambda x: x[1], reverse=True)

    items = [i[0] for i in result]
    real_answer = []
    for n in course:
        com = list(combinations(items, n))
        answer = []
        max = 0
        for i in com:
            menu = ""
            for j in i:
                menu = menu + j
            count = 0
            for k in orders:
                b = 0
                for l in menu:
                    if l in k:
                        pass
                    else:
                        b = 1
                        break
                if b == 1:
                    continue
                count = count + 1

            if count > max:
                max = count
                max_menu = sorted(menu, key=lambda x: x[0])
                max_menu = "".join(max_menu)
                answer = []
                answer.append(max_menu)
            elif count == max:
                max = count
                max_menu = sorted(menu, key=lambda x: x[0])
                max_menu = "".join(max_menu)
                answer.append(max_menu)

        if max < 2:
            continue

        for i in answer:
            real_answer.append(i)

    real_answer = sorted(real_answer, key=lambda x: x)

    return real_answer


info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
peopl=[]
for i in info:
    print(i)
    peopl.append(i)

query2=[]
for i in query:
    i=i.split()
    query2.append(i)

answer=[]
for cmd in query2:

    people = peopl
    for i in range(len(cmd)):
        print(cmd[i],-1)
        if cmd[i] == "and" or cmd[i] == "-":
            continue

        if i == len(cmd) - 1:
            print(-3)
            print(people)
            name = []
            for j in range(len(people)):
                a = people[j].split()[-1]
                print(a, cmd[i], people[j])
                if int(a) >= int(cmd[i]):
                    name.append(people[j])
            print(name, -33)
            people = name
            break

        print(cmd[i])
        name = []
        for j in range(len(people)):
            print(people[j])
            if cmd[i] in people[j]:
                name.append(people[j])
        people = name

    print(people, -1)
    answer.append(len(people))
print(answer)




def solution3(info, query):
    peopl = []
    for i in info:
        peopl.append(i)
    query2 = []
    for i in query:
        i = i.split()
        query2.append(i)


    answer = []
    for cmd in query2:

        people = peopl



        for i in range(len(cmd)):
            if cmd[i] == "and" or cmd[i] == "-":
                continue

            if i == len(cmd) - 1:
                name = []
                for j in range(len(people)):
                    a = people[j].split()[-1]
                    if int(a) >= int(cmd[i]):
                        name.append(people[j])
                people = name
                break


            name = []
            for j in range(len(people)):
                if cmd[i] in people[j]:
                    name.append(people[j])
            people = name

            if len(people)==0:
                break


        answer.append(len(people))

    return answer
