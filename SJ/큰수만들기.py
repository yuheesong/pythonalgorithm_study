def solution(number, k):
    answer = ''
    number = list(number)
    num = number[0]


    for i in range(1, len(number)):
        if len(number) == len(number) - k:
            break

        if number[i] > num:
            pass



    return answer

solution("4177252841", 4)