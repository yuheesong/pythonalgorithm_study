def solution(n):
    l = sum(map(int,str(n)))
    if n%l == 0:
        answer = True
    else:
        answer = False
    return answer

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))