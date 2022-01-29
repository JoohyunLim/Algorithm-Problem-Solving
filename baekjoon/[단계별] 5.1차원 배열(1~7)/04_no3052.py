ans = set()	#중복제거를 위해 set 사용
for i in range(10):
	n = int(input())
	ans.add(n%42)
print(len(ans))