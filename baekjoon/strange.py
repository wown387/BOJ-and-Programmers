

def solution(a):
    d=a
    d1=[]
    for i in range(len(d)):
        if d[i]==" ":
            if d[i-1]==" ":
                d1[-1]=d1[-1]+" "
            else:
                d1.append(" ")
    a = a.split()

    answer = []
    for i in a:
        b = ""
        for j in range(len(i)):
            if j % 2 == 0:
                b = b + i[j].upper()
            else:
                b = b + i[j].lower()
        answer.append(b)

    result=""
    for i in range(len(d1)):
        result=result+answer[i]+d1[i]
    result=result+answer[-1]
    print(result)

    return answer
solution("try hello world")


def solution(a):

    answer = ""
    j = 0
    for i in a:
        if i != " ":
            if j % 2 == 0:
                answer = answer + i.upper()
                j = j + 1
            else:
                answer = answer + i.lower()
                j = j + 1
        else:
            answer = answer + " "
            j = 0

    return answer