from collections import Counter
def solution(id_list, report, k):
    data,notice,stop_user = [],[],[]
    report_overlap_remove = list(set(report))
    answer = [0] * len(id_list)
    for i in report_overlap_remove:
        a,b = i.split(" ")
        data.append([a,b])
        notice.append(b)
    x = dict(Counter(notice))
    for key,value in x.items():
        if value >= k:
            stop_user.append(key)
    for i in range(len(data)):
        if data[i][1] in stop_user:
            answer[id_list.index(data[i][0])] += 1 
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))