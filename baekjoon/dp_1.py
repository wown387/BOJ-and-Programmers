import sys

num=int(sys.stdin.readline())

for i in range(num):
    number=int(sys.stdin.readline())
    count = 0
    sum = [number]
    def cal(a):
        n = []

        for i in a:
            if i > 0:
                n.append(i - 1)
                print(count)
            if i > 1:
                n.append(i - 2)
            if i > 2:
                n.append(i - 3)
        return n, n.count(0)
    while True:
        sum, b = cal(sum)
        count = count + b
        a = max(sum)
        if a == 0:
            break
    print(count)


n,k=map(int,input().split())
c=[int(input()) for i in range(n)]
dp=[0 for i in range(k+1)]
dp[0]=1
for i in c:
    for j in range(i,k+1):
        if j-i>=0:
            dp[j]+=dp[j-i]
            print(dp)
print(dp)