a = int(input())
b = int(input())
c = int(input())
m = list(str(a*b*c)) # m = ['1','7','0','3','7','3','0','0']
# count 함수 사용
for i in range(10):
	print(m.count(str(i)))