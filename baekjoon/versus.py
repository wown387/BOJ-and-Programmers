a,b=map(int,input().split())


i=2
count=0
while True:

    j=1
    while True:

        if i*j>=a:
            print(i*j,-2)
            a=i*j
            break
        j=j+1

    k=1
    while True:

        if i*k>=b:
            print(i*k,-4)
            b=i*k
            break
        k=k+1


    i=i*2
    count=count+1

    if a==b:
        print(count,"count")
        break


def solution(n,a,b):


    i = 2
    count = 0

    while True:
        j = 1
        while True:
            if i * j >= a:
                a = i * j
                break
            j = j + 1


        k = 1
        while True:
            if i * k >= b:
                b = i * k
                break
            k = k + 1


        i = i * 2
        count = count + 1


        if a == b:

            answer=count
            return answer

