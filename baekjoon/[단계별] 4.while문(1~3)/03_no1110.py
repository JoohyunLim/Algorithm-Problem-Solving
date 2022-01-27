n = int(input())
newNum = n
count = 0
while True:
	a = newNum//10	#첫째자릿수
	b = newNum%10	#둘째자릿수	
	c = (a+b)%10	#합의 끝자릿수
	newNum = int(str(b)+str(c))	#새 숫자 생성
    
	count += 1	#사이클 길이+1
	if(newNum == n):
		break
print(count)