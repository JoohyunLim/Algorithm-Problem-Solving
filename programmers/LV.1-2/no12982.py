def solution(d, budget):
    cnt = 0
    d.sort()
    for i in range(len(d)):
        if d[i]<=budget:
            cnt+=1
            budget-=d[i]
        else:
            break    
    return cnt