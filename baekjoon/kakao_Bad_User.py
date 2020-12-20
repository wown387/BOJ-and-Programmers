userid=["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id=["fr*d*", "*rodo", "******", "******"]
u_id=['fradi', 'crodo', 'abc123', 'frodoc']

def match_id(u_id,banned_id):
    for i, j in zip(u_id, banned_id):
        if len(i) != len(j):
            return False
        else:
            for k in range(len(i)):
                if j[k] == "*":
                    continue
                elif i[k] != j[k]:
                    return False
    return True


from itertools import permutations

a=permutations(userid,len(banned_id))
answer=[]
for i in a:
    a=set(i)
    if match_id(i, banned_id):
        if a not in answer:
            print(i)
            answer.append(a)


print(answer)

a=('frodo', 'fradi', 'abc123', 'frodoc')
b=('frodo', 'fradi', 'frodoc', 'abc123')
a=set(a)
b=set(b)
print(a==b)


from itertools import permutations


def match_id(u_id,banned_id):
    for i, j in zip(u_id, banned_id):
        if len(i) != len(j):
            return False
        else:
            for k in range(len(i)):
                if j[k] == "*":
                    continue
                elif i[k] != j[k]:
                    return False
    return True
def solution(user_id, banned_id):
    id_list = permutations(user_id, len(banned_id))
    answer = []
    for i in id_list:
        id_set = set(i)
        if match_id(i, banned_id):
            if id_set not in answer:
                answer.append(a)
    return len(answer)