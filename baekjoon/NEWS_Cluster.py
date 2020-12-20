
import collections

def cal(str1,str2):
    s1 = collections.Counter(str1)
    s2 = collections.Counter(str2)
    s3 = set(list(s1.keys()) + list(s2.keys()))

    gyo = []
    hap = []
    for i in s1:
        for j in range(min(s1[i], s2[i])):
            gyo.append(i)

    for i in s3:
        for j in range(max(s1[i], s2[i])):
            hap.append(i)

    return len(gyo),len(hap)

def solution(str1, str2):
    st1 = []
    st2 = []
    str1 = str1.upper()
    str2 = str2.upper()
    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            st1.append(str1[i:i + 2])
        else:
            pass
    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            st2.append(str2[i:i + 2])
        else:
            pass

    a, b = cal(st1, st2)
    if a == 0 and b == 0:
        answer = 65536
    else:
        answer = int((a / b) * 65536)
    return answer


import re
import math

def other_solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)



#---------------------------------------------------------------
# First fail solution

str1="handshake"
str2="shake hands"


def cal(str1):
    n_str1 = ""
    for i in str1:
        n_str1 = n_str1 + i.upper()

    result = []
    for i in range(len(n_str1) - 1):
        a = n_str1[i:i + 2]
        b = ""
        c = 0
        for j in a:

            if (ord(j) >= 65 and ord(j) <= 90) or (ord(j) >= 97 and ord(j) <= 122):
                b = b + j
            else:
                c = 1
                break
        if c == 0:
            result.append(b)
    return  result

def solution(str1, str2):
    p_str1 = cal(str1)
    p_str2 = cal(str2)
    print(p_str1,p_str2)

    n_s1 = len(p_str1)
    n_s2 = len(p_str2)

    if n_s1 > n_s2:

        result = set(p_str1)

        for i in p_str2:
            result.add(i)

        print(result)

        set1 = []

        for i in result:
            a1 = p_str1.count(i)
            b1 = p_str2.count(i)

            if a1 > b1:
                for j in range(a1):
                    set1.append(i)
            else:
                for j in range(b1):
                    set1.append(i)
        print(set1)

        for i in p_str2:
            if i not in p_str1:
                set1.append(i)

        set2 = []

        for i in p_str2:
            for j in p_str2:
                if i == j:
                    set2.append(i)
                    break


    else:
        result = set(p_str2)

        for i in p_str1:
            result.add(i)

        print(result)

        set1 = []

        for i in result:
            a1 = p_str2.count(i)
            b1 = p_str1.count(i)

            if a1 > b1:
                for j in range(a1):
                    set1.append(i)
            else:
                for j in range(b1):
                    set1.append(i)
        print(set1)

        set2 = []


        for i in p_str1:
            for j in p_str2:
                if i == j:
                    print(i, j)
                    set2.append(i)
                    break

    if len(set2) == 0 and len(set1)!=0:

        answer = 0
    elif len(set2)==0 and len(set1)==0:

        answer=65536

    else:

        answer = int(len(set2) / len(set1) * 65536)
    print(answer)
    return answer

solution(str1,str2)





