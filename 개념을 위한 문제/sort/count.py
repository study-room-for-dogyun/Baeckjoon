n = int(input())
array = list(map(int, input().split()))


def count_sort(arr):
    temp = [0] * (max(arr) + 1)

    for i in range(len(arr)):
        temp[arr[i]] += 1

    result = []
    for i in range(len(temp)):
        for j in range(temp[i]):
            result.append(i)

    return result

print(count_sort(array))