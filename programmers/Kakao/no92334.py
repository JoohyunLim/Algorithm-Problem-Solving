from collections import defaultdict

def solution(id_list, report, k):
    
    dic= defaultdict(list)
    count = defaultdict(int)
    result = []

    #딕셔너리에 신고자 : 신고된 자 저장
    for i in report:
        reporter, reportee = i.split()
        if(reportee not in dic[reporter]):  #reporter가 reportee를 이미 신고한 내역이 없으면
            dic[reporter].append(reportee)  #신고자 딕셔너리 value에 신고된 자 저장
            count[reportee] +=1 #신고된 자 횟수 +1

    #k번 이상 신고된 유저 찾기, 신고자에게 안내 +1
    for i in id_list:   # muzi, frodo, apeach, neo 순서
        res = 0
        for user in dic[i]: #frodo, neo(muzi가 신고한 애들), neo(frodo가 "), frodo, muzi(apeach가 "), (neo가 "(없음))
            if count[user] >= k:    #신고 횟수가 k회 이상이면 +1
                res += 1
        result.append(res)  #id_list 순서대로 결과 담기
    return result