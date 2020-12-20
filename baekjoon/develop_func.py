progresses=[93,30,55]
speeds=[1,1,1]


def solution(progresses, speeds):
    sum = 0
    answer = []
    cnt = 0
    while True:
        for j in range(cnt,len(progresses)):
            progresses[j] = progresses[j] + speeds[j]

        print(progresses)

        if progresses[cnt] >= 100:
            count = 0
            for k in range(cnt,len(progresses)):
                if progresses[k] >= 100:
                    count = count + 1
                    cnt = cnt + 1
                    speeds[k] = 0
                    progresses[k] = 0
                else:
                    break
            answer.append(count)
            sum=sum+count



        if sum==len(progresses):
            break

    print(answer)

    return answer

solution(progresses,speeds)