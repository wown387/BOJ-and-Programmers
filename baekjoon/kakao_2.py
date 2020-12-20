cmd=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
def solution(cmd):
    com = []
    name = {}
    for i in cmd:
        cmd1 = i.split()
        if cmd1[0] != "Change":
            com.append((cmd1[0], cmd1[1]))
        if cmd1[0] == "Enter" or cmd1[0] == "Change":
            name[cmd1[1]] = cmd1[2]
    result = []
    for i in com:
        a = name[i[1]]
        if i[0] == "Enter":
            result.append("%s님이 들어왔습니다." % a)
        else:
            result.append("%s님이 나갔습니다." % a)
    return result