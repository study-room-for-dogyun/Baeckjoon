# https://www.acmicpc.net/problem/1037

n = int(input())
divide = list(map(int, input().split()))
print(max(divide) * min(divide))
