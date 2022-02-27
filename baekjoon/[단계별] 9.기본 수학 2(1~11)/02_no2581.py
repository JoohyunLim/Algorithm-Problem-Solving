m = int(input())
n = int(input())
sosu = []
for i in range(m, n+1):
    if i != 1:
        isSosu = True
        for j in range(2, i):
            if i % j == 0:
                isSosu = False
                break
        if isSosu:
            sosu.append(i)
if len(sosu) == 0:
    print(-1)
else:
    print(sum(sosu))
    print(sosu[0])