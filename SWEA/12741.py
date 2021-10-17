# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXuUo_Tqs9kDFARa&categoryId=AXuUo_Tqs9kDFARa&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

T = int(input())
case = [list(map(int, input().split())) for _ in range(T)]
ans = []

for a, b, c, d, in case:
    t = min(b, d) - max(a, c)
    if t > 0:
        ans.append(t)
    else:
        ans.append(0)

for i in range(len(ans)):
    print(f"#{i+1} {ans[i]}")