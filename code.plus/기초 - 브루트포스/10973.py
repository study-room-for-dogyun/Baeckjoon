# https://www.acmicpc.net/problem/10973

n = int(input())
p = list(map(int, input().split()))

def x(per):
    for idx in range(n-1, 0, -1):
        if per[idx-1] > per[idx]:
            for k in range(n-1, idx-1, -1):
                if per[idx-1] > per[k]:
                    per[k], per[idx-1] = per[idx-1], per[k]
                    return per[:idx] + sorted(per[idx:], reverse=True)
    return [-1]

print(" ".join(list(map(str, x(p)))))