import heapq

def cal(scoville):
    a =heapq.heappop(scoville)
    b =heapq.heappop(scoville)
    scoville.append(a + b * 2)


    return  scoville

def solution(scoville, k):
    heapq.heapify(scoville)
    count = 0
    while True:
        if len(scoville) < 2 or scoville[0] >= k:
            break

        scoville = cal(scoville)
        count = count + 1

    if scoville[0]>=k:
        answer=count
    else:
        answer=-1
    print(answer)
    return answer

