n=int(input())
arr = list(map(int, input().split()))

def reverse(x):
    return int(str(x)[::-1])

def isPrime(x):
    if x==1:
        return False
    for i in range (2, x):
        if x%i==0:
            return False
    return True

for i in range(n):
    arr[i] = reverse(arr[i])
    if isPrime(arr[i]):
        print(arr[i], end=' ')