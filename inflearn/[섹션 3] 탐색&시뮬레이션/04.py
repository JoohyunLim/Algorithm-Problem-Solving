n1 = int(input())
list1 = list(map(int, input().split()))
n2 = int(input())
list2 = list(map(int, input().split()))
# list1 뒤에 list2를 붙인 후 정렬
list1 = sorted(list1.__add__(list2))
for i in list1:
    print(i,end=" ")