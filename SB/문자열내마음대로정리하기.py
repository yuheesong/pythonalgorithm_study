from collections import deque
def solution(strings, n):
    answer = list()
    d = list(deque([(str,str[n]) for str in strings]))
    d.sort(key=lambda x:(x[1],x))
    for i in d:
        answer.append(i[0])
    return answer

print(solution(["sun", "bed", "car"],1))
print(solution(["abce", "abcd", "cdx"],2))