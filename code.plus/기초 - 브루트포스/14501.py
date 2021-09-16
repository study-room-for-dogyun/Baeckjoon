# https://www.acmicpc.net/problem/14501

# INPUT
n = int(input())

t = []
p = []
answer = [0] * (n + 1)

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)


# Solution
for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        answer[i] = answer[i + 1]
    else:
        answer[i] = max(p[i] + answer[i + t[i]], answer[i + 1])
        

# OUTPUT
print(answer[0])