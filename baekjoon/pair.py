


def cal(s):
    answer=s[:]

    for i in range(len(s) - 1):
        a = s[i:i + 2][0]
        b = s[i:i + 2][1]
        print(s[i:i + 2], a, b)
        if a == b:
            answer=s[:i]+s[i+2:]
            return answer
    return answer

def solution(s):
    while True:
        s1 = s[:]
        s = cal(s)
        if len(s) == 0:
            answer=1
            break
        elif s1 == s:
            answer=0
            break
    print(answer)
    return answer

s="baabaa"

def cal1(s):
    s1 = s[:]

    for i in range(len(s) - 1):
        a = s[i:i + 2][0]
        b = s[i:i + 2][1]
        print(s[i:i + 2])
        if a == b:
            print(s[i], s[i + 1])
            s1 = s1[:i] + "11" + s[i + 2:]
            print(s1)
    if s1==s:
        return s1

    print(s1)
    s1 = s1.replace("1", "")
    return s1

def cal2(s):
    num=[]
    for i in range(len(s) - 1):
        a = s[i:i + 2][0]
        b = s[i:i + 2][1]
        print(s[i:i + 2])
        if a == b:
            print(s[i], s[i + 1])
            num.append(s[1],s[i+1])


    return

cal(s)


def solution1(s):
    while True:
        s1 = s[:]
        s = cal1(s)
        if len(s) == 0:
            answer=1
            break
        elif s1 == s:
            answer=0
            break
    print(answer)
    return answer






s="Cbaabaa"

s=list(s)

i=len(s)-1
while True:

    if s[i]==s[i+1]:
        print(i,-1)
        del s[i]
        del s[i]
        i=len(s)-2
        print(-3)
        continue

    if len(s)==0:
        print(1)
        break

    i = i-1
    print(s)


s = list("babaa")

def solution(s):
    while True:
        result = []
        for i in range(len(s) - 1):

            if s[i] != 0 and s[i] != s[i + 1]:

                result.append(s[i])
            elif s[i] == s[i + 1]:
                s[i] = 0
                s[i + 1] = 0

        if len(s) > 0 and s[-1] != 0:
            result.append(s[-1])

        if result == s:
            print(s)
            break
        else:
            s = result


    if len(s) == 0:
        print(1)
        answer=1
    else:
        print(0)
        answer=0


    return answer

solution(s)

from collections import deque


def cal(s):
    que_s = deque(s)
    answer = ""
    i = 0
    while True:
        if len(que_s) <2:
            for j in que_s:
                answer=answer+j
            break
        if que_s[i] != que_s[i + 1]:
            answer = answer + que_s[i]
            que_s.popleft()
        else:
            que_s.popleft()
            que_s.popleft()

    if s==answer:
        return -1

    return answer
def solution(s):
    while True:
        s = cal(s)
        if s == -1:
            return 0
        elif len(s)==0:
            return  1


s="cdcd"
print(solution(s))



s="baabaa"

s_stack=[]

for i in s:
    print(i)

    if len(s_stack)==0:
        s_stack.append(i)
    elif s_stack[-1]==i:
        del s_stack[-1]
    else:
        s_stack.append(i)
    print(s_stack)

if len(s_stack)==0:
    print(1)
else:
    print(0)

def solution(s):
    s_stack = []

    for i in s:
        if len(s_stack) == 0:
            s_stack.append(i)
        elif s_stack[-1] == i:
            del s_stack[-1]
        else:
            s_stack.append(i)

    if len(s_stack) == 0:
        return 1
    else:
        return 0

