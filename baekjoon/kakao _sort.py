
files=["F-5 Freedom Fighter","B-50 Superfortress","A-10 Thunderbolt II","F-14 Tomcat"]
files= ["muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT"]

files2=[]
for file in files:
    inx = []
    for i in range(1, len(file)):
        if file[i].isdigit():
            inx.append(i)
        if file[i].isalpha() and len(inx) > 0:
            break

    file = [file[:inx[0]], file[inx[0]:inx[len(inx) - 1] + 1], file[inx[len(inx) - 1] + 1:]]
    files2.append(file)

def upper(x):
    return  x[0].lower()

file2=sorted(files2,key=lambda x: (upper(x),int(x[1])) )
print(file2)
answer=[]
for i in file2:
    i="".join(i)
    answer.append(i)
print(answer)


def upper(x):
    return x[0].lower()


def solution(files):
    files2 = []
    for file in files:
        inx = []
        for i in range(1, len(file)):
            if file[i].isdigit():
                inx.append(i)
            if file[i].isalpha() and len(inx) > 0:
                break

        file = [file[:inx[0]], file[inx[0]:inx[len(inx) - 1] + 1], file[inx[len(inx) - 1] + 1:]]

        files2.append(file)

    try:
        file2 = sorted(files2, key=lambda x: (upper(x), int(x[1])))
    except:
        file2 = sorted(files2, key=lambda x: upper(x))

    a = []
    for i in file2:
        i = "".join(i)
        a.append(i)
    return a


def upper(x):
    return x[0].lower()


def solution(files):
    files2 = []
    for file in files:
        inx = []
        for i in range(1, len(file)):
            if file[i].isdigit():
                inx.append(i)
            if file[i].isalpha() and len(inx) > 0:
                break

        file = [file[:inx[0]], file[inx[0]:inx[len(inx) - 1] + 1], file[inx[len(inx) - 1] + 1:]]

        files2.append(file)

    try:
        file2 = sorted(files2, key=lambda x: (upper(x), int(x[1])))
    except:
        file2 = sorted(files2, key=lambda x: upper(x))

    a = []
    for i in file2:
        i = "".join(i)
        a.append(i)
    return a