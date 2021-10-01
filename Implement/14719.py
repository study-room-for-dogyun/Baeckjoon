# https://www.acmicpc.net/problem/14719

h, w = map(int, input().split())
world = list(map(int, input().split()))

answer = 0
for cur in range(1, w-1):

    left_max = max(world[0:cur])
    right_max = max(world[cur+1:])
    rain = min(left_max, right_max) - world[cur]

    if rain <= 0:
        continue

    answer += rain

print(answer)
