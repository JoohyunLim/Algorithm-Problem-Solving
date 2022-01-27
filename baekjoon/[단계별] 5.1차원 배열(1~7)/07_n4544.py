C = int(input())
for i in range(C):
	scores = list(map(int, input().split()))
	n = scores[0]
	scores = scores[1:]
	ave = sum(scores)/n

	cnt = 0	#평균을 넘는 학생 수
	for j in scores:
		if j>ave:
			cnt+=1
	print("%.3f%%" %(cnt/n*100))