def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0,0,0]

    for i in range(len(answers)):
        i1 = i %5
        i2 = i %8
        i3 = i%10
        if answers[i] == a[i1] : count[0] += 1 
        if answers[i] == b[i2] : count[1] += 1 
        if answers[i] == c[i3] : count[2] += 1 
    maxcount = max(count[0],count[1],count[2])
    if maxcount == count[0]: answer.append(1)
    if maxcount == count[1]: answer.append(2)
    if maxcount == count[2]: answer.append(3)
    return answer

print(solution([1,2,3,4,5]))