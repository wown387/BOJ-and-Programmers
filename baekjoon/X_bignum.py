

expression="100-200*300-500+20"
expression=list(expression)
oper=[]
oper_li="*+-"
for i in range(len(expression)):
    if expression[i] in oper_li:
        oper.append(i)
print(oper)
print(expression)

for i in range(len(expression)):
    if expression[i]=="+":
        a=oper.index(i)
        if oper[a-1]==0:
            o1 = oper[0]
            o2 = oper[a + 1]
        elif oper[a+1]==len(expression)-1:
            o1 = oper[a - 1]
            o2 = oper[len(expression-1)]
        else:
            o1 = oper[a - 1]
            o2 = oper[a + 1]

        expression[o1]=expression[o1]+"("
        expression[o2]=")"+expression[o2]
print(expression)

