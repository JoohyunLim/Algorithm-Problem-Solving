#입력처리
n, k = map(int, input().split())
answer = []

for i in range(1, n+1):
	if n%i == 0:
		answer.append(i)

if len(answer) >= k:	#k번째 수가 존재하면
	print(answer[k-1])
else:
	print(-1)