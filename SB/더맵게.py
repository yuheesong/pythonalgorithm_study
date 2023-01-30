import heapq

def solution(scoville, K):
    n = 0 
    heapq.heapify(scoville)
    if scoville[0] > K:
        return -1
    while scoville[0] < K:
        try:
            temp1 = heapq.heappop(scoville)
            temp2 = heapq.heappop(scoville)
            re = temp1 + temp2*2
            heapq.heappush(scoville,re)
            n = n + 1
        except IndexError:
            n = -1 
            break
    return n



'''
def solution(scoville, K):
    n = 0
    scoville.sort()
    while scoville[0] < K or scoville[1] < K:
        temp = list()
        temp.append(scoville[0] + scoville[1]*2)
        scoville = temp + scoville[2:]
        n = n + 1
    return n
'''
print(solution([1, 2, 3, 9, 10, 12],7))