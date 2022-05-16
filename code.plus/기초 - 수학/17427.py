# https://www.acmicpc.net/problem/17427

N = int(input())

answer = 0
for i in range(1, N + 1):
    answer += (N // i) * i

print(answer)