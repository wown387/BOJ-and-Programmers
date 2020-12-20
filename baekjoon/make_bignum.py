
k=2
a="1942"


number="4177252841"
k=3

anwer_n=len(number)-k
answer=""
ind = 0
while True:
    a = len(number) - k
    max = 0
    for i in range(ind, len(number) - a + 1):
        print(number[i:i + a])
        if max < int(number[i:i + a][0]):
            max = int(number[i:i + a][0])
            ind = i+1

    print(max, ind)

    answer = answer + str(max)
    k=k+1

    if len(answer)==anwer_n:
        break
print(answer)

def solution(number, k):
    anwer_n = len(number) - k
    answer = ""
    ind = 0
    while True:
        a = len(number) - k
        max = 0
        for i in range(ind, len(number) - a + 1):
            print(number[i:i + a])
            if max < int(number[i:i + a][0]):
                max = int(number[i:i + a][0])
                ind = i + 1
            if int(number[i:i + a][0])==9:
                max=9
                ind=i+1
                break



        answer = answer + str(max)
        k = k + 1

        if len(answer) == anwer_n:
            break

    return answer


def solution(a, k):

    b = len(a)

    while True:

        c=a[:]
        if len(a) == b - k :
            break
        for i in range(k):
            if i+1>len(a)-1:
                break
            if a[i+1]==9:
                a = a[:i] + a[i + 1:]
                break
            if a[i] < a[i + 1]:
                a = a[:i] + a[i + 1:]
                break

        if c==a:
            a=a[:-1]

    print(a)
    answer = a
    return answer

solution(a,k)