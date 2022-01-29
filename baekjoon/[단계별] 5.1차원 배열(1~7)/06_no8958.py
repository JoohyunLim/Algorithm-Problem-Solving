N = int(input())
for i in range(N):
	arr = list(input())
	score = 0	#총점수
	plusscore = 1	#누적점수
	for j in arr:
		if j == "O":
			score += plusscore
			plusscore += 1
		elif j == 'X':
			plusscore = 1
	print(score)