import collections

def solution(clothes):
    answer = 1
    clothe_type = []
    
    for i in range(len(clothes)):
	    clothe_type.append(clothes[i][1])   # ex: ['headgear', 'eyewear', 'headgear']
   
    numOfClothes = list(collections.Counter(clothe_type).values())    # numOfClothes=[2,1]
    
    for j in range(len(numOfClothes)):
            answer = (answer*((numOfClothes)[j]+1))   # 각 요소에 1씩 더하고 모두 곱하기 
        
    return (answer-1)   # 아무것도 입지 않은 경우 빼기