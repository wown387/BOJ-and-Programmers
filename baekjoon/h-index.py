
a=[36,61]



def solution(a):
    a.sort()

    max = 0
    for i in range(len(a)):
        print(len(a) - i, a[i])
        b = (len(a) - i, a[i])
        if a[i] >= len(a) - i and len(a) - i > max:
            max = len(a) - i

    return max

"""def solution(a):
    a.sort()
    max = None
    for i in a:
        print((len(a)-a.index(i)),i)

        if (len(a) - a.index(i)) >= i :
            max =i

    print(max)
    return max
solution(a)"""