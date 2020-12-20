def solution(m,d):
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    day_ = "FRI"
    sum=0
    for i in range(m-1):
        sum=sum+mon[i]-28

    a = (day.index(day_)+sum)%7

    d1=(d-1+a)%7

    answer=day[d1]

    print(m,d,day[d1])

    return answer

solution(4,22)


