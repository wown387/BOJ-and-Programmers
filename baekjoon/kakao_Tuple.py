s="{{4,2,3},{3},{2,3,4,1},{2,3}}"
s=s.replace("{","")
s=s.split("}")[:-2]
s_li=[]
for i in s:
    i=i.split(",")
    li=[]
    for j in i:
        if j.isdigit():
            li.append(j)
    s_li.append(li)
c=sorted(s_li,key=lambda x:len(x))
print(c)
answer=[]
for i in c:
    for j in i:
        if int(j) not in answer:
            answer.append(int(j))
            break
print(answer)

def solution(s):
    s = s.replace("{", "")
    s = s.split("}")[:-2]
    s_li = []
    for i in s:
        i = i.split(",")
        li = []
        for j in i:
            if j.isdigit():
                li.append(j)
        s_li.append(li)
    c = sorted(s_li, key=lambda x: len(x))
    answer = []
    for i in c:
        for j in i:
            if j not in answer:
                answer.append(int(j))
                break

    return answer





