def solution(s):
    word=[]
    a=s.split()
    for i in a:
        w = ""
        for j in range(len(i)):
            if j%2==0:
                w=w+i[j].upper()
            else:
                w=w+i[j].lower()
        word.append(w)
    answer=" ".join(word)
    answer="%s" %answer
    return answer

def solution(phone_number):
    b=phone_number[-4:]
    a="*"*(len(phone_number)-4)+b
    answer = a
    return answer


def solution(participant, completion):
    answer = ''
    print(participant)
    print(completion)
    b=0
    for i in range(len(participant)):
        if b==1:
            break
        for j  in range(len(completion)):
            if participant[i]==completion[j]:
                completion[j]=1
                break
            if participant[i] not in completion:
                answer=participant[i]
                b=1
                break
    for i in participant:
        if b==1:
            break
        if i!=1:
            print(i)
            break
    return answer

def cal(a):
    a[-2] = a[-1] + a[-2] * 2
    del a[-1]
    a.sort(reverse=True)

    return a


def solution(scoville, K):
    num=0
    answer = 0
    while True:
        print(scoville)
        if len(scoville) == 1 and scoville[0] < K:
            answer = -1
            break

        if scoville[-1] >= K:
            break
        else:
            scoville = cal(scoville)
            answer = answer + 1

    return answer

print(solution([1,2],3))





a=["mislav", "stanko", "mislav", "ana"]
b=["stanko", "ana", "mislav"]
solution(a,b)

anwer=solution("027778888")
print(anwer)
