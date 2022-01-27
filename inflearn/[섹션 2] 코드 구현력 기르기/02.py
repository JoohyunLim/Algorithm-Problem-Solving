numOfCase=int(input())	#케이스의 개수

for i in range(numOfCase):
    n, s, e, k = map(int, input().split())	#띄어쓰기를 기준으로 읽어들임
    arr = list(map(int, input().split()))	#리스트에 숫자열 저장
    arr = arr[s-1:e]	#s번째부터 e번째까지의 수
    arr.sort()	#오름차순 정렬
    print("#%d %d" %(i+1, arr[k-1]))