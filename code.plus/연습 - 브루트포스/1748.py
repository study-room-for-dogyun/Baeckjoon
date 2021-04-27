# https://www.acmicpc.net/problem/1748

n = int(input())

result = 0
k = 0   # 자리수
for i in range(8, -1, -1):
    if n >= 10 ** i:
        k = i
        break

for i in range(1, k+1):
    result += i * (10**i - 10**(i-1))

result += (k+1) * (n - 10**k + 1)
print(result)