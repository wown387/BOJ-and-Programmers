s="3people unFollowed me"
s=s.lower()
s=list(s)
s[0]=s[0].upper()
for i in range(len(s)-1):
    if s[i]==" "and s[i+1]!=" ":
        s[i+1]=s[i+1].upper()
s="".join(s)
print(s)



def solution(s):
    s = s.lower()
    s = list(s)
    s[0] = s[0].upper()
    for i in range(len(s) - 1):
        if s[i] == " " and s[i + 1] != " ":
            s[i + 1] = s[i + 1].upper()
    s = "".join(s)


    return s

