n = int(input())

def fibo(x):
    temp = [0, 1, 1]

    for i in range(3, x + 1):
        temp.append(temp[i-1] + temp[i-2])
    
    return temp[x]

print(fibo(n))