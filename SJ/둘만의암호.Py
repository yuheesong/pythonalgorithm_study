def solution(s, skip, index):
    answer = ''

    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

    s = list(s)
    skip = list(skip)

    count = 0

    for i in range(len(s)):
        start_idx = alphabet_list.index(s[i])
        final_idx = start_idx + 6
        check_list = alphabet_list[start_idx+1:final_idx]
        if len(check_list) < index:
            plus_list_idx = index - len(check_list)
            check_list += alphabet_list[:plus_list_idx]

        for i in range(len(check_list)):
            if check_list[i] in skip:
                check_list.remove(check_list[i])
                check_list.append(alphabet_list[i+(index+1)])
        answer += check_list[-1]
        
    return answer


print(solution("aukks", "wbqd", 5 ))