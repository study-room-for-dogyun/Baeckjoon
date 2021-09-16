# https://www.acmicpc.net/problem/15664
from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
check = set()
for i in combinations(nums, m):
    if i not in check:
        print(" ".join(list(map(str, i))))
        check.add(i)
