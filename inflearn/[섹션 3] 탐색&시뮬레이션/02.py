import re
txt = input()
cnt = 0
txt = re.sub('[^\d]','',txt)    #숫자가 아닐 경우 제거
while txt.startswith('0'):  #0으로 시작할 경우 제거
    txt = txt[1:]
# txt의 약수의 개수 구하기
for i in range (1,int(txt)+1):
    if int(txt) % i == 0:
        cnt += 1
print(txt, cnt, sep="\n")