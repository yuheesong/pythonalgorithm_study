def solution(arr):
    compare_number = arr[0]
    re = list()
    re.append(compare_number)
    for i in range(1,len(arr)):
        if compare_number == arr[i]:
            pass
        else:
            compare_number = arr[i]
            re.append(arr[i])
    return re

print(solution([1, 1, 3, 3, 0, 1, 1]))