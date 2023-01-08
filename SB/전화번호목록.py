"""

#내가 푼거 
def solution(phone_book):
    answer = True
    result = list()
    #for i in range(len(phone_book)):
    check = min(phone_book)
    for p in phone_book:
        result.append(p[:len(check)])
    if len(result) != len(set(result)):
         answer = False
    return answer
"""
#남이 푼거 
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i,j in zip(phone_book,phone_book[1:]):
        if j.startswith(i):
            answer = False
    return answer

#hash 남이 푼거 
'''
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
'''


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]	))
