# https://www.acmicpc.net/problem/15665

from itertools import product, repeat

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
nums = list(product(nums, repeat=m))
nums = sorted(list(set(nums)))

for i in nums:
    print(*i)


# nums = list(set(nums))
# nums.sort()
# over = set()

# def dfs(value, length):
#     global nums

#     if length == m and value not in over:
#         over.add(value)
#         print(" ".join(value))
#         return
    
#     for num in nums:
#         dfs(value+str(num), length+1)

# for i in nums:
#     dfs(str(i), 1)
