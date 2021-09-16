# https://www.acmicpc.net/problem/11723
import sys
input = lambda: sys.stdin.readline().rstrip()
print = sys.stdout.write

m = int(input())
s = 0

for _ in range(m):
    oper = input().split()
    if len(oper) == 1:
        o = oper[0]
    else:
        o, x = oper[0], int(oper[1])-1

    if o == 'add':
        s |= 1<<x
    elif o == 'remove':
        s &= ~(1<<x)
    elif o == 'check':
        print('1\n' if s & 1<<x else '0\n')
    elif o == 'toggle':
        s ^= 1<<x
    elif o == 'all':
        s = 2**20 - 1
    else:
        s = 0
