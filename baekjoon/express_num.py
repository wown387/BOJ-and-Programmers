
n=5


def solution(n):
    answer = []

    for i in range(1, n//2+2):

        x = (n + (i * (i - 1) / 2)) / i


        if x == int(x):
            answer.append(i)
        if int(x)-(i-1)==1:

            print(answer)
            return len(answer)
    print(answer)
    return len(answer)

solution(n)