num1 = int(input())
num2 = int(input())

a = int(str(num2)[0])	//num2의 첫째 자릿수
b = int(str(num2)[1])	//num2의 둘째 자릿수
c = int(str(num2)[2])	//num2의 셋째 자릿수

print(num1*c)
print(num1*b)
print(num1*a)
print(num1*num2)