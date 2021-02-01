n = []
while True:
    temp = int(input())
    if temp == 0:
        break
    else:
        n.append(temp)

def sosu(n):
    if n == 1:
        return False

    for i in range(3, n):
        if n % i == 0:
            return False

    return True


def goldbach(n):
    for i in range(3, n//2, 2):
        if sosu(i) and sosu(n-i):
            return f"{n} = {i} + {n-i}"

    return "Goldbach's conjecture is wrong."

    
for i in n:
    print(goldbach(i))