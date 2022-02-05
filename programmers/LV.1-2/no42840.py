def solution(answers):
    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5]
    n3 = [3,3,1,1,2,2,4,4,5,5]
    cnt = [0]*3
    answer = []
    
    for i in range (len(answers)):
        if answers[i] == n1[i%len(n1)]:
            cnt[0] += 1
        if answers[i] == n2[i%len(n2)]:
            cnt[1] += 1
        if answers[i] == n3[i%len(n3)]:
            cnt[2] += 1
    
    for i in range (len(cnt)):
        if cnt[i] == max(cnt):
            answer.append(i+1)
    
    return answer