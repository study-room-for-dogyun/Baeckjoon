# NO Brute-Force
# NO Greedy
# USE DP
# 물건을 부분적으로 담을 수 없다.
# 각 물건은 모두 한개 씩만 있다.

# n = 물건 개수
# k = 최대 가방 무게
n, k = map(int, input().split())

# [무게, 가치]
wv = []
for _ in range(n):
    wv.append(list(map(int, input().split())))

# print(max(wv, key=lambda x: x[1])[1])
dp = []
for _ in range((max(wv, key=lambda x: x[1])[1])):
    dp.append([0] * n)


