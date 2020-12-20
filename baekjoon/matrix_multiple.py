arr1=[[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2=[[5, 4, 3], [2, 4, 1], [3, 1, 1]]

answer=[]
for i in arr1:
    result=[]
    for j in range(len(arr1)):
        print(i)
        sum=0
        for k in range(len(arr2)):
            print(arr2[k][j])
            sum=sum+i[k]*arr2[k][j]
        print(sum)
        result.append(sum)
    answer.append(result)
print(answer)


def solution(arr1, arr2):
    answer = []
    for i in arr1:
        result = []
        for j in range(len(arr2)):
            sum = 0
            for k in range(len(arr2[0])):
                sum = sum + i[k] * arr2[k][j]
            result.append(sum)
        answer.append(result)
    return answer

def solution(arr1, arr2):
    answer = []
    for i in arr1:
        result = []
        for j in range(len(arr2[0])):
            sum = 0
            for k in range(len(arr2)):
                sum = sum + i[k] * arr2[k][j]
            result.append(sum)
        answer.append(result)
    return answer