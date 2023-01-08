def solution(clothes):
    dic = dict()
    sum = 1

    for r in clothes:
        name,type = r
        
        if type in dic:
            dic[type].append(name)
        else:
            dic[type] = [name]

    for i in dic.values(): 
        sum *= len(i)+1
    return sum-1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	))