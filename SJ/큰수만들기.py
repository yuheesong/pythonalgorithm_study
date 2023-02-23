# def solution(number, k):
#     answer = ''
#     stack = []
#     for digit in number:
#         while k > 0 and stack and stack[-1] < digit:
#             stack.pop()
#             k -= 1
#         stack.append(digit)
#     answer = ''.join(stack[:len(stack)-k])
#     return answer

# print(solution("4177252841", 4))


#stack, pop 
def solution(number, k):
    answer = ''
    stack = []
    for digit in number:
        while k > 0 and stack and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    answer = ''.join(stack[:len(stack)-k])
    return answer

print(solution("4177252841", 4))

# 99876 

#zfill -> 몇자리수를 나타내줌 
