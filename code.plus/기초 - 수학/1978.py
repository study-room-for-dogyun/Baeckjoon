n = int(input())

num = list(map(int, input().split()))

result = 0

def sosu(n):

    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


for i in num:
    if sosu(i):
        result += 1


print(result)