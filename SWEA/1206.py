# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

for _ in range(10):
    n = int(input())
    bl = list(map(int, input().split()))
    answer = 0
    for i in range(2, n-2):
        temp = min(bl[i] - bl[i-2], bl[i] - bl[i-1], bl[i] - bl[i+1], bl[i] - bl[i+2])
        if temp < 0:
            continue
        answer += temp
    print(answer)