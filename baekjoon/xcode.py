def cal(bag):
    result = []
    for i in range(len(bag)):

        if len(bag)==1:
            result.append(bag[0])
            break

        else:
            if i==0 and bag[0]!=bag[1]:
                result.append(bag[0])
            elif i==len(bag)-1 and bag[i-1]!=bag[i]:
                result.append(bag[i])

            elif i>0 and bag[i]!=bag[i-1] and bag[i]!= bag[i+1]:
                result.append(bag[i])





    print(result)
    return result

##인형뽑

a=[4, 3, 1, 1, 3, 2, None, 4]
b=cal(a)
print(b)




def pick(n, board):
    p = 0
    for i in board:

        if i[n - 1] != 0:
            p = i[n - 1]
            i[n - 1] = 0
            break
    return p

def solution(board, moves):
    bag = []
    count = 0
    for i in moves:

        if len(bag)>1 and bag[-2]==bag[-1]:
            del bag[-1]
            count=count+1
        else:
            bag.append(pick(i, board))
    print(count*2)
    return count*2



def solution(board, moves):
    moved = []
    count = 0
    for x in moves:
        for i in range(len(board)): #board's row
            c = x-1    #choosed cul
            if board[i][c] != 0:
                got = board[i][c]
                board[i][c] = 0
                if len(moved) == 0:
                    moved.append(got)
                elif len(moved) > 0 and got != moved[-1]:
                    moved.append(got)
                else:
                    count += 1
                    del moved[-1]
                break
    return count*2


##추석 트래


lin=[
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s",
]

def cal(line):
    a = line.split()

    b = a[1].split(":")

    total_e = int(b[0]) * 60 * 60 + int(b[1]) * 60 + float(b[2])

    total_s = total_e - float(a[2][:-1])

    return (total_s,total_e)




def solution(lin):

    line = []

    for i in lin:
        line.append(cal(i))

    print(line)
    start = line[0][0]
    for i in line:
        if i[0] < start:
            start = i[0]
    print(start)
    end = line[-1][1]
    for i in line:
        if i[1] > end:
            end = i[1]
    print(end)

    start = int(start)
    end = int(end)
    print(start, end)
    max=0
    max_i=0
    for i in range(start, end + 2):
        aa = set()
        for j in line:
            if j[0] <= i and j[1] >= i:
                aa.add(j[0])

        for j in line:
            if j[0] <= i + 1 and j[1] >= i + 1:
                aa.add(j[0])
        if len(aa)>max:
            max=len(aa)
            max_i=i

    print(max,max_i)


    answer = 0
    return answer

solution(lin)