# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    temp=-1
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(arr)):
        if arr[i] != temp:
            temp = arr[i]
            answer.append(arr[i])
    return answer

print(solution([1,1,3,3,0,1,1]))#	[1,3,0,1]
print(solution([4,4,4,3,3]))#	[4,3]