
def solution(x):
    sum=0
    for i in str(x):
        sum+=int(i)
    if x%sum==0:
        return True
    return False
solution(10)