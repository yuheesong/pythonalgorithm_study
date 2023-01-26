def solution(a, b, n):
    answer = 0
    while n >= a:
        quotient  = n//a
        remainder = n%a
        answer += quotient*b
        n = (quotient*b)+remainder 
    return answer

print(solution(3,2,20))