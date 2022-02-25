hour,min = map(int, input().split())
t = int(input())

if (min+t)//60:
    hour += (min+t)//60
    min = (min+t)%60
else:
    min += t

while hour >= 24:
    hour %= 24
print(hour, min)