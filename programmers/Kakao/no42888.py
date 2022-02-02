from collections import defaultdict

def solution(record):
    id_name = defaultdict(list)
    result = []
    answer = []
    
    #각 요소를 끊어 담아 2차원 리스트 만들기
    #ex) result = [['Enter', 'uid1234', 'Muzi'], ['Enter', 'uid4567', 'Prodo'],...]
    for i in record:
        result.append(i.split())

    #id_name 딕셔너리에 {id : 닉네임} 저장/변경
    for i in result:
        if i[0] == 'Enter' or i[0] == 'Change':
            id_name[i[1]] = i[2]
       
    #최종 닉네임으로 enter, leave 메시지 설정
    for i in result:
        if i[0] == 'Enter':
            answer.append(str(id_name[i[1]]) + "님이 들어왔습니다.")  
        elif i[0] == 'Leave':
            answer.append(str(id_name[i[1]]) + "님이 나갔습니다.")  

    return answer