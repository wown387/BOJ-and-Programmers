


brown = 8
yellow= 1

result=[]

for i in range(1,yellow):
    print(i)

    if yellow%i==0:
        if i >yellow//i:
            break
        result.append((i,yellow//i))

if yellow==1:
    result.append((1,1))

print(result)



for i in result:

    num_brown=(i[0]+2)*2+(i[1]+2)*2-4

    print(i,num_brown)

    if num_brown==brown:

        answer=[i[1]+2,i[0]+2]

print(answer)

def solution(brown, yellow):
    result = []

    for i in range(1, yellow):


        if yellow % i == 0:
            if i > yellow // i:
                break
            result.append((i, yellow // i))

    if yellow == 1:
        result.append((1, 1))


    for i in result:

        num_brown = (i[0] + 2) * 2 + (i[1] + 2) * 2 - 4


        if num_brown == brown:
            answer = [i[1] + 2, i[0] + 2]


    return answer