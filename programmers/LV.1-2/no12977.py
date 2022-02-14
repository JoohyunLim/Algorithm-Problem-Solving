from itertools import combinations

def isPrime(x):
    if x==1:
        return False
    for i in range (2, x):
        if x%i==0:
            return False
    return True
    
def solution(nums):
    cnt = 0
    arr = list(combinations(nums, 3))
    # nums 가 [1,2,3,4] 일 경우
    # arr는 [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
    for a, b, c in arr: 
        if isPrime(a+b+c):
            cnt += 1
    return cnt