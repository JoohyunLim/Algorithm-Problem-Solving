def digit_sum(x):
	return sum(list(map(int,str(x))))	#list로 변환하지 않고 sum 사용 가능

N = int(input())
arr = list(map(int, input().split()))
max = -9999999
answer = 0

for i in arr:
	dsum = digit_sum(i)
	if dsum>max:
		max = dsum
		answer = i
print(answer)