# https://www.acmicpc.net/problem/14500

# INPUT
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


# Solution

# 1. 폴리오미노 형태 정의
x = 0
y = 0

def a(x, y):
    return [[x, y], [x+1, y], [x+2, y], [x+3, y]]
def b(x, y):
    return [[x, y], [x+1, y], [x, y+1], [x+1, y+1]]
def c(x, y):
    return[[x, y], [x, y+1], [x, y+2], [x+1, y+2]]
def d(x, y):
    return [[x, y], [x, y+1], [x+1, y+1], [x+1, y+2]]
def e(x, y):
    return [[x, y], [x+1, y], [x+2, y] ,[x+1, y+1]]


print(a(2, 3))