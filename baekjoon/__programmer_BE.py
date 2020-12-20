from collections import Counter
votes=["AAD", "AAA", "AAC", "AAB"]
votes=["AVANT", "PRIDO", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "AVANT", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "SOULFUL", "AVANT", "SANTA"]

a=Counter(votes)
print(a)

b=a.items()

c=sorted(b,key=lambda x: (-x[1],x[0]))
print(c)

k=2
sum=0
for i in range(k):
    sum=sum+c[i][1]
print(sum)

answer=""
for i in reversed(c):
    print(i)
    sum=sum-i[1]
    if sum<=0:
        break
    answer=i[0]
print(answer)

from collections import Counter

def solution(votes, k):
    a = Counter(votes)
    b = list(a.items())
    c = sorted(b, key=lambda x: (-x[1], x[0]))

    sum = 0
    for i in range(k):
        sum = sum + c[i][1]
    answer = ""
    for i in reversed(c):
        sum = sum - i[1]
        if sum <= 0:
            break
        answer = i[0]

    return answer


p="AM 12:01:00"

p="PM 11:59:59"
p="PM 01:00:00"
p="PM 05:05:05"
p="AM 13:01:00"
n=0
p=p.split()

if p[0]=="PM" and int(p[1][:2])<=12:
    p1=list(map(int,p[1].split(":")))
    p1[0]=p1[0]+12

elif p[0]=="AM" and  int(p[1][:2])>=12:
    p1 = list(map(int, p[1].split(":")))
    p1[0] = p1[0] + -12
else:
    p1 = list(map(int, p[1].split(":")))

total=p1[0]*60*60+p1[1]*60+p1[2]+n

if total>=86400:
    total=total%86400
    a=total//(60*60)
    b=(total%(60*60))//60
    c=((total%(60*60))//60)%60
    print(a,b,c,"00")

else:
    a = total // (60 * 60)
    b = (total % (60 * 60)) // 60
    c = ((total % (60 * 60)) % 60)
    print(a, b, c,str(00))

answer=[]
d=[str(a),str(b),str(c)]

for i in d:
    if len(i)==1:
        answer.append("0{}".format(i))
    else:
        answer.append(i)
print(":".join(answer))
answer=":".join(answer)


def solution(p, n):
    p = p.split()

    if p[0] == "PM" and int(p[1][:2]) < 12:
        p1 = list(map(int, p[1].split(":")))
        p1[0] = p1[0] + 12

    elif p[0] == "AM" and int(p[1][:2]) >= 12:
        p1 = list(map(int, p[1].split(":")))
        p1[0] = p1[0] - 12

    else:
        p1 = list(map(int, p[1].split(":")))

    total = p1[0] * 60 * 60 + p1[1] * 60 + p1[2] + n

    if total >= 86400:
        total = total % 86400
        a = total // (60 * 60)
        b = (total % (60 * 60)) // 60
        c = (total % (60 * 60)) % 60

    else:
        a = total // (60 * 60)
        b = (total % (60 * 60)) // 60
        c = ((total % (60 * 60)) % 60)

    answer = []

    d = [str(a), str(b), str(c)]

    for i in d:
        if len(i) == 1:
            answer.append("0{}".format(i))
        else:
            answer.append(i)
    answer = ":".join(answer)

    return answer

p="AM 12:01:00"
p="PM 11:59:59"


print(solution(p,200000))