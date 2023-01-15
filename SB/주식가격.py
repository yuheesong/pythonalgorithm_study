from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    while queue:
        temp = 0
        n = queue.popleft()
        for q in queue:
            temp += 1
            if n > q:
                break
        answer.append(temp)
    return answer

print(solution([1, 2, 3, 2, 3]))