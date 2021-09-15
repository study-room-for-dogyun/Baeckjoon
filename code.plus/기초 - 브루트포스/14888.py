# https://www.acmicpc.net/problem/14888
# from itertools import permutations

n = int(input())
num = list(map(int, input().split()))
oper = list(map(int, input().split()))
# oper = '+'*l[0] + '-'*l[1] + '*'*l[2] + '/'*l[3]

maxi = -9999999999
mini = 9999999999

# for o in permutations(oper):

#     temp = num[0]
#     for idx in range(len(o)):
#         if o[idx] == '+':
#             temp += num[idx+1]
#         elif o[idx] == '-':
#             temp -= num[idx+1]
#         elif o[idx] == '*':
#             temp *= num[idx+1]
#         else:
#             if temp < 0:
#                 temp = abs(temp) // num[idx+1]
#                 temp *= -1
#             else:
#                 temp //= num[idx+1]

#     maxi = max(maxi, temp)
#     mini = min(mini, temp)

# print(maxi)
# print(mini)

def dfs(value, depth, idx, plus, minus, multi, divide):

    global maxi, mini

    if depth == n-1:
        maxi = max(maxi, value)
        mini = min(mini, value)

    else:
        if plus:    # 숫자 0이면 False 아니면 True
            dfs(value + num[idx], depth+1, idx+1, plus-1, minus, multi, divide)
        if minus:
            dfs(value - num[idx], depth+1, idx+1, plus, minus-1, multi, divide)
        if multi:
            
            dfs(value * num[idx], depth+1, idx+1, plus, minus, multi-1, divide)
        if divide:
            if value < 0:
                dfs(-(abs(value) // num[idx]), depth+1, idx+1, plus, minus, multi, divide-1)
            else:
                dfs(value // num[idx], depth+1, idx+1, plus, minus, multi, divide-1)

dfs(num[0], 0, 1, *oper)
print(maxi, mini, sep='\n')