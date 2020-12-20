def solution(board):

    sum = 0
    for i in board:
        for j in i:
            sum = sum + j
    if sum == 0:
        return 0
    max=0
    for z in board:
        n=z.count(1)
        if n>max:
            max=n
    print(max)


    a = len(board)
    b = len(board[0])

    result = [a, b]
    k = min(result)

    for k in reversed(range(k + 1)):
        answer = 0
        for l in range(len(board) - k + 1):
            for m in range(len(board[0]) - k + 1):

                d = 0
                sum=0
                for i in range(k):
                    if d == 1:
                        break
                    for j in range(k):
                        if board[i + l][j + m] == 0:
                            d = 1
                            break
                        else:
                            sum=sum+1
                if sum==k * k:
                    answer = k * k
                    print(answer)
                    return answer



board=[[0,0,0,0],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
board1=[[0,0,1,1],[1,1,1,1]]
for i in board:
    print(i)
solution(board)