N=int(input())
arr = list(input())
score = 0	#총점수
plusscore = 1	#누적점수
for i in arr:
	if i == "1":
		score += plusscore
		plusscore += 1
	elif i == '0':
		plusscore = 1
print(score)