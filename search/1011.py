# https://www.acmicpc.net/problem/1011

t = int(input())

for _ in range(t):

    x, y = map(int, input().split())

    # 0부터 시작해서 반틈 위치까지는 최대로 땡기기
    # 반틈 위치부터 한 칸씩 내려가서 최종적으로 1 되게 하기
    

    result = 0

    distance = y - x
    exp = 0
    while True:
        if 2**exp <= distance < 2**(exp+1):
            break
        exp += 1

    s = (exp*(exp+1)) // 2

    if distance >= 2*s:

        distance -= s
        result += exp

        while True:
            if distance < s:
                break
            distance -= s
            result += exp
        
        if distance % exp == 0:
            result += distance // exp
        else:
            result += distance // exp + 1
    
    else:
        distance -= s
        result += exp


    print(result)
