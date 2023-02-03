from collections import deque

def solution(n, words):
    num = 1
    count = 1
    answer = 0
    stack = list() 
    while True:
        if words == []:
            answer = [0,0]
            break
        if num == n+1: 
            num = 1
            count +=1
        if stack == []:
            stack.append(words.pop(0))
            num += 1
            continue
        if words[0] in stack or words[0].strip()[0] != stack[-1].strip()[-1]:
            answer = [num,count]
            break
        else:
            stack.append(words.pop(0))
            num += 1
    return answer

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))