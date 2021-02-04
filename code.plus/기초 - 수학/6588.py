import sys
input = lambda: sys.stdin.readline().rstrip()

maxi = 1000001
n = []
chk = [True] * maxi

while True:
    temp = int(input())
    if temp == 0:
        break
    else:
        n.append(temp)


# 에라토스테네스의 체 
# 소수의 배수는 소수가 아니다 
# -> 소수가 나오면 그 배수를 제외시킴
m = int(maxi ** 0.5)
for i in range(2, m+1):
    if chk[i] == True:
        for j in range(i+i, maxi, i):
            chk[j] = False


def goldbach(n):
    global chk
    
    for i in range(2, n//2):
        if chk[i] and chk[n-i]:
            return f"{n} = {i} + {n-i}"

    return "Goldbach's conjecture is wrong."

    
for i in n:
    print(goldbach(i))