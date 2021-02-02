n = [int(input()) for _ in range(9)]

def solve(arr):
    for i in range(8):
        for j in range(i+1, 9):
            temp1, temp2 = arr[i], arr[j]
            arr[i], arr[j] = 0, 0

            print(arr)
            if sum(arr) == 100:
                return arr

            arr[i], arr[j] = temp1, temp2
            
n = solve(n)
n.sort()
for i in n[2:]:
    print(i)