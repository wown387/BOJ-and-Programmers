expression="100-200*300-500+20"

oper="*+-"



expression=expression.split(oper[2])

result=[]
for i in expression:
    a=i.split(oper[1])

    answer=[]
    for j in range(len(a)):
        a[j]=str(eval(a[j]))
        answer.append(a[j])
    answer=oper[1].join(answer)

    result.append(answer)

result=oper[2].join(result)
print(result)
print(eval(result))

