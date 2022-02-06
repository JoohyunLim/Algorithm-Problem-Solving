N=int(input())
sum = 0
max_sum = 0
for i in range (N):
    d1, d2, d3=list(map(int, input().split()))
    if d1==d2==d3:
        sum=10000+d1*1000
    elif d1==d2 or d1==d3:
        sum=1000+d1*100
    elif d2==d3:
        sum=1000+d2*100
    else:
        sum=max(d1,d2,d3)*100
    if sum>max_sum:
        max_sum = sum
print(max_sum)