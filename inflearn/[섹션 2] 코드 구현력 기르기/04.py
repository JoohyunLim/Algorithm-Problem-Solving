n = int(input())
scores = list(map(int, input().split()))

average = round(sum(scores)/n)	#평균 반올림
min = 100
temp = []

# '평균과의 점수차 절대값'이 가장 작은 경우를 구해 min 변수에 저장
for i in range(n):
	if abs(scores[i]-average) < min:
		min = abs(scores[i]-average)

# '평균과의 점수차 절대값'이 min인 경우의 점수들을 temp 리스트에 저장
for i in range(n):
	if abs(scores[i]-average) == min:
		temp.append(scores[i])

# temp의 숫자들 중 가장 큰 숫자를 가진 학생의 번호 출력 (여러 명일 경우 앞 번호의 학생)
for i in range(n):
	if scores[i] == max(temp):
		print(average, i+1)
		break;