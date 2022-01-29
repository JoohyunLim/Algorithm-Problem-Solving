n=int(input())
numList=[True]*(n+1)
numList[0]=False    #0,1은 제외
numList[1]=False
cnt=0

for i in range(2, n+1):
    if numList[i] == True:    #True면 소수
        cnt+=1
        for j in range(i+i, n+1, i):  #소수 i의 배수들은 모두 제외(False)
            numList[j] = False;
print(cnt)