def solution(s):
    answer = 0
    str = list(s)
    for i in str:
        if i == '(':
            answer -= 1 
        elif i == ')':
            answer += 1
        if answer > 0:
            return False 

    return True if answer == 0 else False

print(solution('(())'))