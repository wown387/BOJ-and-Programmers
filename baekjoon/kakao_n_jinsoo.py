
def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, t, m, p):
    answer=""
    count = 0
    count_1 = 0
    i = 0
    while True:
        if m == p:
            p = 0
        con_i = convert(i, n)

        for j in range(len((con_i))):
            count = count + 1

            if count % m == p:
                count_1 = count_1 + 1
                answer = answer + con_i[j]
                print(con_i[j], count, count_1, -1)
            else:
                print(con_i[j])

            if count_1 == t:
                return answer
        i = i + 1



m=2
p=2
n=16
t=16
print(solution(n,t,m,p))
