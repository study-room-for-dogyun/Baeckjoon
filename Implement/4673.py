# https://www.acmicpc.net/problem/4673

l = [True] * 10001

for n in range(1, 10001):

    while n < 10000:
        n += n//1000 + (n%1000)//100 + (n%100)//10 + n%10
        
        if n > 10000 or not l[n]:
            break

        l[n] = False

for i in range(1, 10001):
    if l[i]:
        print(i)