def solution(n, lost, reserve):
    answer = 0
    lost.sort(reverse=True)
    reserve.sort(reverse=True)

    for i in range(len(reserve)):
        if reserve[i] + 1 in lost:
            lost.remove(reserve[i]+1)
            continue
        if reserve[i] - 1 in lost:
            lost.remove(reserve[i]-1)
            continue
    answer = n - len(lost)
    return answer

print(solution(6, [3, 4], [1, 6, 5]))