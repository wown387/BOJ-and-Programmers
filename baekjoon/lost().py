
num=input()



if "-" in num:
    a=num.index("-")

    num1=num[:a]
    num2=num[a+1:].replace("+","-")

    num1=num1.split("+")

    num2=num2.split("-")


    sum=0
    for i in num1:
        sum=sum+int(i)
    sum2=0
    for i in num2:
        sum2=sum2+int(i)

    answer=-sum2+sum
    print(answer)


else:
    a=num.split("+")
    sum=0
    for i in a:
        sum=sum+int(i)
    print(sum)


