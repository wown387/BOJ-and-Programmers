board=["CCBDE", "AAADE", "AAABF", "CCBBF"]
board_row=[]

board1=[]
for i in range(len(board[0])):
    board1_1=[]
    for j in reversed(board):
        board1_1.append(j[i])
    board1.append(board1_1)
#대칭변경
for i in board1:
    print(i,-1)


def cal(board1):
    count=0
    change = []
    for i in range(len(board1) - 1):
        for j in range(len(board1[0]) - 1):
            print(board1[i][j], board1[i][j + 1], board1[i + 1][j], board1[i + 1][j + 1])
            if board1[i][j] == board1[i][j + 1] == board1[i + 1][j] == board1[i + 1][j + 1]:
                change.append([i, j])
    # 바꿔야 할 인덱

    for i in change:
        if board1[i[0]][i[1]].isalpha():
            board1[i[0]][i[1]] = ""
            count=count+1
        if board1[i[0] + 1][i[1]].isalpha():
            board1[i[0] + 1][i[1]]= ""
            count = count + 1
        if board1[i[0]][i[1] + 1].isalpha():
            board1[i[0]][i[1] + 1] = ""
            count = count + 1
        if board1[i[0] + 1][i[1] + 1].isalpha():
            board1[i[0] + 1][i[1] + 1] = ""
            count = count + 1
    # 바꾸기

    cal_board = []
    for i in board1:
        n = i.count("")
        i = "".join(i) + "0" * n
        cal_board.append(list(i))
    return cal_board,count



count=0
while True:
    board1, cnt = cal(board1)
    count=count+cnt

    if cnt==0:
        break


def cal(board1):
    count=0
    change = []
    for i in range(len(board1) - 1):
        for j in range(len(board1) - 1):
            print(board1[i][j], board1[i][j + 1], board1[i + 1][j], board1[i + 1][j + 1])
            if board1[i][j] == board1[i][j + 1] == board1[i + 1][j] == board1[i + 1][j + 1]:
                change.append([i, j])
    # 바꿔야 할 인덱

    for i in change:
        if board1[i[0]][i[1]].isalpha():
            board1[i[0]][i[1]] = ""
            count=count+1
        if board1[i[0] + 1][i[1]].isalpha():
            board1[i[0] + 1][i[1]]= ""
            count = count + 1
        if board1[i[0]][i[1] + 1].isalpha():
            board1[i[0]][i[1] + 1] = ""
            count = count + 1
        if board1[i[0] + 1][i[1] + 1].isalpha():
            board1[i[0] + 1][i[1] + 1] = ""
            count = count + 1
    # 바꾸기

    cal_board = []
    for i in board1:
        n = i.count("")
        i = "".join(i) + "0" * n
        cal_board.append(list(i))
    return cal_board,count



def solution(m, n, board):
    board1 = []
    for i in range(len(board)):
        board1_1 = []
        for j in reversed(board):
            board1_1.append(j[i])
        board1.append(board1_1)

    count=0
    while True:
        board1, cnt = cal(board1)
        count = count + cnt
        if cnt == 0:
            break
    answer = count
    return answer

print(solution(4,5,board))