card = []
for i in range(21): #카드 채우기
    card.append(i)

for i in range(10): #카드 구간 뒤집기
    a, b = map(int, input().split())
    card[a:b+1] = card[a:b+1][::-1]

for n in card[1:]:  #카드 출력하기
    print(n,end=' ')