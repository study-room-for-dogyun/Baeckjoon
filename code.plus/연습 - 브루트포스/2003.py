# https://www.acmicpc.net/problem/2003

n, m = map(int, input().split())
l = list(map(int, input().split()))

if sum(l) < m:
    print(0)
    exit()
if sum(l) == m:
    print(1)
    exit()

result = 0
for i in range(n):
    for j in range(i, n):
        s = sum(l[i:j+1])
        if s > m:
            break
        if s == m:
            result += 1
            break

print(result)