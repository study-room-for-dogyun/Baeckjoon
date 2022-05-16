T = int(input())

for _ in range(T):
    t = int(input())
    scores = list(map(int, input().split()))

    bindo = [0] * 101

    for i in scores:
        bindo[i] += 1

    answer = []
    m = max(bindo)
    for idx, i in enumerate(bindo):
        if i == m:
            answer.append(idx)

    print(f"#{t} {answer[-1]}")
