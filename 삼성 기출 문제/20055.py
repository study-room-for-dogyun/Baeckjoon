# https://www.acmicpc.net/problem/20055

N, K = map(int, input().split())
A = [99] + list(map(int, input().split()))
belt = [99] + [0] * (2 * N)


def rotate():
    a1 = A[-1]
    b1 = belt[-1]
    for i in range(2 * N, 1, -1):
        A[i] = A[i - 1]
        belt[i] = belt[i - 1]
    A[1] = a1
    belt[1] = b1


ans = 0
while A.count(0) < K:
    ans += 1

    rotate()

    # 내리기
    belt[N] = 0

    # 로봇 움직이기
    for i in range(2 * N, 0, -1):
        if belt[i] == 1 and belt[i % (2 * N) + 1] == 0 and A[i % (2 * N) + 1] > 0:
            belt[i] = 0
            belt[i % (2 * N) + 1] = 1
            A[i % (2 * N) + 1] -= 1
    belt[N] = 0

    # 로봇 올리기
    if belt[1] == 0 and A[1] != 0:
        belt[1] = 1
        A[1] -= 1

print(ans)
