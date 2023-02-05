def solution(citations):
    max_list = list()
    answer = 0 
    citations.sort(reverse=True)
    while True:
        if citations == []:
            break 
        max_list.append(citations.pop(0))
        newList  = [x for x in citations if x >= max_list[-1]]
        if max_list[-1] >= len(newList)+len(max_list):
            answer = max_list[-1]
    return answer

print(solution([3, 0, 6, 1, 5]))