from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
idxs = list(map(int, input().split()))
dq = deque([i for i in range(1, n+1)])
answer = 0
for i in idxs:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        if dq.index(i) < len(dq)/2:
            dq.rotate(-1)
            answer = answer + 1
            continue
        else:
            dq.rotate(1)
            answer = answer + 1
            continue
print(answer)