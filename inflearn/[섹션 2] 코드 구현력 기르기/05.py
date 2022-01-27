import collections
n, m = map(int, input().split())
arr = []

for i in range(1,n+1):
	for j in range(1,m+1): 
		arr.append(i+j)		# N + M의 모든 경우의 수 저장

arr = collections.Counter(arr)		# 숫자와 발생 빈도를 딕셔너리에 저장
max = max(sorted(list(arr.values())))	# 가장 높은 발생 빈도 (ex.4회)

for i in range(len(arr)):
	if (list(arr.values())[i] == max):	# 가장 높은 발생 빈도를 가질 경우
		print(list(arr.keys())[i])	# key값 출력