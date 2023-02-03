def solution(skill, skill_trees):
    count = 0 
    for st in skill_trees:
        temp = []
        for str in st:
            if str in skill:
                temp.append(str)
        temp = ''.join(temp)
        if skill[:len(temp)] == temp:
            count += 1
    return count

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))