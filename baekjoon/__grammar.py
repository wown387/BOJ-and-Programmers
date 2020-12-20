a=list(range(1,10))
import string
a=list(string.ascii_uppercase)
a="12"
b="123"
a="1234"
print(a[::-1])
from collections import defaultdict
d={"a":10}
print(d)

d=defaultdict(lambda :0)
d["Wrong"]=10
print(d["hona"])
print(d,-1)


print(b.startswith(a))

import pwd

a=pw

import re
pattern="phone"
textt="asdfasdf"
mathch=re.search(pattern,text)
mathch.span()
re.findall(pattern,text)
import re
text="hello worl1d11"

pattern="world"
match=re.search(r"\d\d",text)
print(match)


# 소수
import math

def isPrime(num):
    if num == 1: return False
    n = int(math.sqrt(num))
    for k in range(2, n+1):
        if num % k == 0:
            return False
    return True


for i,index in enumerate(a):
    print(i,index)
list1=[1,2,3]
list2=["a","b","c"]
list3=["q","w","e"]
for i in zip(list1,list2,list3):
    print(i,-1)


#중복이 리스트에서 없앨
a=[1,2,3,1,3]
a=set(a)
print(a)

b=[]
for i in a:
    if i not in a:
        b.append(i)

from itertools import combinations,product

items=[i for i in range(5)]

com=list(combinations(items,3))
print(type(com[1]))

num=product(a,repeat=int(b))

def add(name):
    print(  f"hello {name}"  )

add("jane")

import random

for i in range(10):
    n = random.randint(0, 22)
    a.append(n)

a=[1,2,3,4,5]

for i in reversed(a):
    print(i)





def solution(numbers):
    a = list(map(str, a))

    a.sort(key=lambda x: x * 3, reverse=True)

    answer = "".join(a)


    return answer

"""map(def,list)

filter(conditon,list)"""

import collections

participant=["mislav", "stanko", "mislav", "ana"]
completion=["stanko", "ana", "mislav"]

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)

    return list(answer.keys())[0]

