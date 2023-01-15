def solution(progresses, speeds):
    answer = []
    
    for i,j in zip(progresses,speeds):
        if len(answer) == 0 or answer[-1][0] < (-((i-100)//j)):
            answer.append([-((i-100//j)),1])
        else:
            answer[-1][1] += 1
    return [x[1] for x in answer]

'''
#답지
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
'''
print(solution([93, 30, 55],[1, 30, 5]))