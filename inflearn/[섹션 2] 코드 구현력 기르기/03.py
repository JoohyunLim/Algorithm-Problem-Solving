n, k = map(int, input().split())	#첫 줄에 주어진 n, k 입력받기
cards = list(map(int, input().split()))		#카드열 입력받기
answer=[]

for i in range(n):
	for j in range(i+1, n):
		for m in range(j+1, n):
			if (cards[i]+cards[j]+cards[m]) not in answer:
				answer.append(cards[i]+cards[j]+cards[m])

answer.sort()
print(answer[-k])