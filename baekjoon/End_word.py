word=["hello", "one", "even", "never", "now", "world", "draw"]

n=2

result=[]
answer=[word[0]]
for i in range(2,len(word)+1):
    print(word[i-1])

    if word[i-2][-1]==word[i-1][0] and word[i-1] not in answer:
        answer.append(word[i-1])

    else:
        if i%n==0:
            num=n
            num2=i//n
        else:
            num=i%n
            num2=i//n+1

        result=[num,num2]

        break
if len(result)==0:
    result=[0,0]
print(result)

def solution(n, word):
    result = []
    answer = [word[0]]
    for i in range(2, len(word) + 1):
        print(word[i - 1])

        if word[i - 2][-1] == word[i - 1][0] and word[i - 1] not in answer:
            answer.append(word[i - 1])

        else:
            if i % n == 0:
                num = n
                num2 = i // n
            else:
                num = i % n
                num2 = i // n + 1

            result = [num, num2]

            break
    if len(result) == 0:
        result = [0, 0]
    print(result)

