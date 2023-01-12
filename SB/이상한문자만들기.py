def solution(s):
    result = list()
    word = s.split(' ')
    for w in word:
        result.append(change(w))
    return ' '.join(result)

def change(word):
    w_list = list(word)
    for i in range(len(w_list)):
        if i%2 == 0:
            w_list[i] = w_list[i].upper() 
        else:
            w_list[i] = w_list[i].lower()
    return ''.join(w_list)
print(solution("try hello world"))