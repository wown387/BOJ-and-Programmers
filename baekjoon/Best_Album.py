genres=["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]
songs={}
songs_in={}
index=0
for i,j in zip(genres,plays):
    print(i,j)
    if songs.get(i)==None:
        songs[i]=[]
        songs[i].append([index,j])
    else:
        songs[i].append([index,j])
    index=index+1


print(songs)

def cal(a):
    print(a)
    sum=0
    for i in a:
        sum=sum+i[1]
    return sum

songs=sorted(songs.items(),key=lambda x: cal(x[1]),reverse=True)
print(songs,-1)
answer=[]
for i in songs:
    i=sorted(i[1],key=lambda x:x[1],reverse=True)
    print(i)
    if len(i)<2:
        answer.append(i[0][0])
    else:
        answer.append(i[0][0])
        answer.append(i[1][0])
print(answer)


def cal(a):
    sum = 0
    for i in a:
        sum = sum + i[1]
    return sum

def solution(genres, plays):
    songs = {}
    index = 0
    for i, j in zip(genres, plays):
        if songs.get(i) == None:
            songs[i] = []
            songs[i].append([index, j])
        else:
            songs[i].append([index, j])
        index = index + 1

    songs = sorted(songs.items(), key=lambda x: cal(x[1]), reverse=True)
    answer = []
    for i in songs:
        i = sorted(i[1], key=lambda x: x[1], reverse=True)
        if len(i) < 2:
            answer.append(i[0][0])
        else:
            answer.append(i[0][0])
            answer.append(i[1][0])
    return answer