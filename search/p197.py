import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
n_arr = sorted(list(map(int, input().split())))

m = int(input())
m_arr = sorted(list(map(int, input().split())))

print(n_arr, m_arr)

def binary_search(arr, key, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, start, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, end)


for i in m_arr:
    if binary_search(n_arr, i, 0, n - 1) is None:
        print('no', end=' ')
    else:
        print('yes', end=' ')