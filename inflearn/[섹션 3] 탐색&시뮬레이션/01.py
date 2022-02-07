n=int(input())
for i in range(n):
    text = input().lower()
    if text == text[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))