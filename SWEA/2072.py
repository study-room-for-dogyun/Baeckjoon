# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

t = int(input())
for _ in range(t):
    answer = 0
    l = list(map(int, input().split()))
    for i in l:
        if i % 2 == 1:
            answer += i
    print(answer)