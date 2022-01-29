m, n = map(int, input().split())
numList=[True]*(n+1)
numList[0] = False
numList[1] = False

for i in range(2, n+1):
    if numList[i] == True:    #True면 소수
        for j in range(i+i, n+1, i):  #소수 i의 배수들은 모두 제외(False)
            numList[j] = False

for i in range(m,n+1):
    if numList[i] == True:
        print(i)