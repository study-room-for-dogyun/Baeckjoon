# https://www.acmicpc.net/problem/4375

while True:
    try:
        N = int(input())
    except EOFError:
        break

    one = '1'
    while True:
        if int(one) % N == 0:
            print(len(one))
            break

        one += '1'