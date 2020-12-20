
def solution(a):
    b = []
    c = 0
    for i in range(len(a)):

        b.append((len(str(a[i])),a[i],i))

    b.sort(reverse=True)
    print(b)
    for i in reversed(b):
        if c == 1:
            answer = False
            break
        for j in b:
            if str(i[1]) in str(j[1]):
                d=j[1].split(i[1])
                print(d)

    if c == 0:
        answer = True

    print(answer)
    print(b)
    return answer

a=["12","123","1235","567","88"]
def solution(a):
    d=0
    c = True
    a.sort()
    for i in range(len(a)):
        if d==1:
            break
        for j in range(i + 1, len(a)):
            if a[i] in a[j]:
                b = a[j].split(a[i])
                if b[0] == "":
                    c = False
                    d=1
                    break

    return c



solution(a)