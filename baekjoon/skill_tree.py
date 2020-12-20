skill_tree=["BACDE", "CBADF", "AECB", "BDA"]
skill="CB"


def solution(skill, skill_tree):
    count = 0
    for j in skill_tree:
        a = []
        for i in skill:
            b = j.find(i)
            if b == -1:
                b = 30
            a.append(b)

        c = a[:]
        a.sort()
        print(c, a, j)
        if c == a:
            count = count + 1
    answer = count
    return answer



