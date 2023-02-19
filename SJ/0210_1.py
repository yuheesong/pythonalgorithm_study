from itertools import permutations
#0, 1, 2, 3, 4, 5, 6, 7, 8, 9

#소수 찾기 공식 
#permutations


def solution(number):
    number_set = set()

    for i in range(len(number)):
        permutation_numbers = permutations(list(number), i+1)
        per_list_numbers = list(map(int, map("".join, permutation_numbers)))
        number_set |= set(per_list_numbers)
    
    number_list = list(number_set)
    number_num = 0
    for i in range(len(number_list)):
        if number_list[i] % 2 == 0 or number_list[i] % 3 == 0 or number_list[i] == 1:
            continue
        
        else:
            number_num += 1

    return number_num

print(solution("011"))