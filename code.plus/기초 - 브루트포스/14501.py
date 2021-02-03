n = int(input())
tp = [list(map(int, input().split())) for _ in range(n)]

maxi = 0
print()
for day in range(n):
    
    bnf = 0
    i = day

    while i < n and i + tp[i][0] <= n:
        print(i, bnf)

        bnf += tp[i][1]

        i += tp[i][0]

    maxi = max(maxi, bnf)
    
    print(maxi, "\n")



print(maxi)