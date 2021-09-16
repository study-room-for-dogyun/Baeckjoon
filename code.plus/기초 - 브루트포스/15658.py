# https://www.acmicpc.net/problem/15658

n = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))

maxi = -10987654321
mini = 10987654321

def dfs(value, depth, idx, plus, minus, multi, divide):
    global maxi, mini

    if depth == n:
        maxi = max(maxi, value)
        mini = min(mini, value)
        return
    
    if plus:
        dfs(value+nums[idx], depth+1, idx+1, plus-1, minus, multi, divide)
    if minus:
        dfs(value-nums[idx], depth+1, idx+1, plus, minus-1, multi, divide)
    if multi:
        dfs(value*nums[idx], depth+1, idx+1, plus, minus, multi-1, divide)
    if divide:
        if value < 0:
            dfs(-(abs(value)//nums[idx]), depth+1, idx+1, plus, minus, multi, divide-1)
        else:
            dfs(value//nums[idx], depth+1, idx+1, plus, minus, multi, divide-1)

dfs(nums[0], 1, 1, *oper)
print(maxi, mini, sep='\n')