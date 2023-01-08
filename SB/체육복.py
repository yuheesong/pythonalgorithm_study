import collections
def solution(n, lost, reserve):
    reserve_n = sorted(list(collections.Counter(reserve) - collections.Counter(lost)))
    lost_n = sorted(list(collections.Counter(lost) - collections.Counter(reserve)))
    answer = n - len(lost_n)
    for i in range(len(lost_n)):   
        if lost_n[i]-1 in reserve_n: 
            answer = answer + 1
            reserve_n.remove(lost_n[i]-1)
        elif lost_n[i]+1 in reserve_n:
            answer = answer + 1
            reserve_n.remove(lost_n[i]+1)
    return answer

print(solution(5,[2, 4],[1, 3, 5]))