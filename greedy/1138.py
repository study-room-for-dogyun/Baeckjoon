n = int(input())
m = list(map(int, input().split()))

line = [0] * n

for i in range(n):

    j = 0
    count = 0
    
    # 0 개수가 맞을 때 까지 증가
    while count != m[i]:
        if line[j] == 0:
            count += 1
        j += 1
    
    # 0 개수가 맞은 자리에서부터 0이 아닌 자리까지 증가
    while line[j] != 0:
        j += 1

    line[j] = i + 1

for i in line:
    print(i, end=" ")
