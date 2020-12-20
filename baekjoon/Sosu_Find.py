from itertools import permutations
import math

def isPrime(num):
    if num == 1: return False
    n = int(math.sqrt(num))
    for k in range(2, n+1):
        if num % k == 0:
            return False
    return True
def solution(n):
    answer=0
    for i in range(1,n+1):
        if isPrime(i):
            answer=answer+1
    return answer

def solution(numbers):
    numbers = list(numbers)
    count = 0
    for i in range(1, len(numbers) + 1):
        numb = permutations(numbers, i)
        numb = set(numb)
        for j in numb:
            n = int("".join(j))
            if isPrime(n) and len(str(n)) == i and n != 0:
                count = count + 1
    answer = count
    return answer


numbers="17"
print(solution(numbers))
