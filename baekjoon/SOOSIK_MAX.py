real_expression="100-200*300-500+20"

from itertools import  permutations
oper="*+-"
oper=list(oper)
oper_li=permutations(oper,3)
answer=0
for oper in oper_li:
    print(oper)
    expression=real_expression
    expression = expression.split(oper[2])
    print(expression)
    expression1 = []
    for i in expression:
        if oper[1] in i:
            i = i.split(oper[1])
            for j in range(len(i)):
                i[j] = str(eval(i[j]))
            i = str(oper[1]).join(i)
        print(i, -1)
        expression1.append(str(eval(i)))

    expression1 = str(oper[2]).join(expression1)
    print(expression1)
    expression1=abs(eval(expression1))
    if answer<expression1:
        answer=expression1

print(answer)

from itertools import permutations
def solution(real_expression):
    oper = "*+-"
    oper = list(oper)
    oper_li = permutations(oper, 3)
    answer = 0
    for oper in oper_li:
        expression = real_expression
        expression = expression.split(oper[2])
        expression1 = []
        for i in expression:
            if oper[1] in i:
                i = i.split(oper[1])
                for j in range(len(i)):
                    i[j] = str(eval(i[j]))
                i = str(oper[1]).join(i)
            expression1.append(str(eval(i)))

        expression1 = str(oper[2]).join(expression1)
        expression1 = abs(eval(expression1))
        if answer < expression1:
            answer = expression1

    return answer