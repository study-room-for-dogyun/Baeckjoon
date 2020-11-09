
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

n, k = map(int, input().split())
array = list(map(int, input().split()))

print(binary_search(array, k, 0, n - 1))