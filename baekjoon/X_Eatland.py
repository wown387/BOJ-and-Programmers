land=[[1,2,3,5],[5,6,7,100], [4,3,2,1]]

def solution(land):
    init_land = [[land[0][0], 0], [land[0][1], 1], [land[0][2], 2], [land[0][3], 3]]
    for i in range(1, len(land)):
        for j in range(len(init_land)):
            land[i][init_land[j][1]] = -land[i][init_land[j][1]]

            init_land[j][0] = init_land[j][0] + max(land[i])
            max_in = land[i].index(max(land[i]))
            land[i][init_land[j][1]] = -land[i][init_land[j][1]]
            init_land[j][1] = max_in

    answer = [init_land[i][0] for i in range(len(init_land))]
    print(answer)
    answer = max(answer)
    return answer
print(solution(land))


def solution2(land):
    answer = 0

    N = len(land)  # N은 행의 개수가 된다.

    for i in range(0, N - 1):
        land[i + 1][0] += max(land[i][1], land[i][2], land[i][3])
        # i+1번째 행에 0번째 열에는 i번째 행에 1,2,3 열 중 최대값을 더해준다. 이런식으로 계속 더해나가면
        # N-1번째에 열들을 각 선택지에서 가질 수 있는 최대값이 된다.

    land[i + 1][1] += max(land[i][0], land[i][2], land[i][3])

    land[i + 1][2] += max(land[i][0], land[i][1], land[i][3])

    land[i + 1][3] += max(land[i][0], land[i][1], land[i][2])


    answer = max(land[N - 1])  # 바로 위에 코드가 똑같은 코드다. N-1행에서의 최대값을 가지는 열 answer에 대입한다.
# answer = max(land[N-1][0],land[N-1][1],land[N-1][2],land[N-1][3])

    return answer

def solution(land):
    N = len(land)  # N은 행의 개수가 된다.

    for i in range(0, N - 1):
        land[i + 1][0] += max(land[i][1], land[i][2], land[i][3])
        # i+1번째 행에 0번째 열에는 i번째 행에 1,2,3 열 중 최대값을 더해준다. 이런식으로 계속 더해나가면
        # N-1번째에 열들을 각 선택지에서 가질 수 있는 최대값이 된다.

    land[i + 1][1] += max(land[i][0], land[i][2], land[i][3])

    land[i + 1][2] += max(land[i][0], land[i][1], land[i][3])

    land[i + 1][3] += max(land[i][0], land[i][1], land[i][2])
    answer = max(land[N - 1])

    return answer