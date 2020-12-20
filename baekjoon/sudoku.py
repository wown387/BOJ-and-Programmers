sudo=[]
for i in range(9):
    num=list(map(int,input().split()))
    sudo.append(num)

def cal1():
    for j in range(9):
        if sudo[j].count(0)==1:
            a=sudo[j].index(0)
            sum=0
            for k in sudo[j]:
                sum=sum+k
            sudo[j][a]=45-sum

def cal2():
    for i in range(9):
        count = 0
        sum=0
        a=0
        b=0
        for j in range(9):
            sum=sum+sudo[j][i]
            if sudo[j][i]==0:
                count=count+1
                a=j
                b=i
            if j==8 and count==1:
                sudo[a][b]=45-sum


def cal3():
    for i in range(0,9,3):
        for j in range(0,9,3):
            count=0
            count1=0
            sum=0
            a=0
            b=0
            for k in range(i,i+3):
                for l in range(j,j+3):
                    count=count+1
                    sum=sum+sudo[k][l]
                    if sudo[k][l]==0:
                        count1=count1+1
                        a=k
                        b=l
                    if count==9 and count1==1:
                        sudo[a][b]=45-sum

while True:
    cal1()
    cal2()
    cal3()
    d=0
    for i in range(9):
        for j in range(9):
            if sudo[i][j]==0:
                d=1
                break
    if d==1:
        continue
    else:
        break




for i in range(len(sudo)):
    for j in range(9):
        if j==8:
            print(sudo[i][j])
        else:
            print(sudo[i][j],end=" ")

