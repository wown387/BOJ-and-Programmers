
def solution(s):
    s = "aabbaccc"
    max = len(s)
    for i in range(1, len(s) // 2 + 1):
        result = []
        j = 0
        while True:
            w = s[j:j + i]

            if len(result) == 0:
                result.append((1, s[j:j + i]))
            elif len(result) > 0 and result[-1][1] == s[j:j + i]:
                result[-1] = (result[-1][0] + 1, w)
            else:
                result.append((1, s[j:j + i]))

            j = j + i

            if j + 1 >= len(s) - 1:
                if len(result) > 0 and result[-1][1] == s[j:j + i]:
                    result[-1] = (result[-1][0] + 1, w)
                else:
                    result.append((1, s[j:]))

                break

        sum = 0
        for i in result:
            if i[0] == 1:
                sum = sum + len(i[1])
            else:
                sum = sum + len(str(i[0])) + len(i[1])



        if max > sum:
            max = sum

    print(max)

    answer = max
    return answer



s="aabbaccc"
max=len(s)
for i in range(1,len(s)//2+1):
    result=[]
    j=0
    print(i)
    while True:
        w=s[j:j+i]

        print(s[j:j+i])
        if len(result)==0:
            result.append((1,s[j:j+i]))
        elif len(result)>0 and result[-1][1]==s[j:j+i]:
            result[-1]=(result[-1][0]+1,w)
        else:
            result.append((1,s[j:j+i]))

        j=j+i


        if j+1>=len(s)-1:
            if len(result) > 0 and result[-1][1] == s[j:j + i]:
                result[-1] = (result[-1][0] + 1, w)
            else:
                result.append((1, s[j:]))

            break
    print(result)

    sum=0
    for i in result:
        if i[0]==1:
            sum=sum+len(i[1])
        else:
            sum=sum+len(str(i[0]))+len(i[1])

    print(sum)

    if max>sum:
        max=sum

print(max)