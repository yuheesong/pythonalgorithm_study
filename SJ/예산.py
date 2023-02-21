def solution(d, budget):

    d.sort()
    answer = 0
    total_budget = 0
    for i in range(0, len(d)):
        if total_budget + d[i] <= budget :
            answer += 1
            total_budget += d[i]
            
    return answer

print(solution([1,3,2,5,4]	, 9))