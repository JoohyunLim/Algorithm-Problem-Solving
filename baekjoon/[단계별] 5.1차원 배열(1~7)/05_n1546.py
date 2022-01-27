n = int(input())
scores = list(map(int, input().split()))
maxscore = max(scores)
for i in range(n):
	scores[i] = scores[i]/maxscore*100
print(sum(scores)/n)