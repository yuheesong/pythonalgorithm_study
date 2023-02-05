def solution(array,commands):
    result = []
    for i in range(len(commands)):
        first = commands[i][0]-1
        last = commands[i][1]
        index = commands[i][2]-1
        slice_list = array[first:last]
        sort_list = sorted(slice_list)
        result.append(sort_list[index])
    return result

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))