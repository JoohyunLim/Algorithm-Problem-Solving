def solution(s):
    answer = ""
    temp = ""
    eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in s:
        if (48<=ord(i)<=57):
            answer += i
        else:
            temp += i
        if (temp in eng):
            answer += str(eng.index(temp))
            temp = ""
    
    return int(answer)