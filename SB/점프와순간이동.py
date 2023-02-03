def solution(n):
    count = 1
    while True:
        if n == 1:
            break
        if n%2 == 0:
            n = n//2
            continue
        else:
            n=n-1
            count +=1 
    return count

'''
def solution(n):
    b = bin(n)
    return b.count('1')
'''
print(solution(5000))