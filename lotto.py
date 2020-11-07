import random

def generate_numbers(n):
    numbers = [random.randrange(1, 46) for _ in range(n)]
    return numbers

def draw_winning_numbers():
    numbers = generate_numbers(6)
    numbers.sort()
    numbers.append(generate_numbers(1)[0])

    return numbers

def count_matching_numbers(list1, list2):
    count = 0
    for i in list1:
        for j in list2:
            if i == j:
                count += 1
    
    return count

def check(numbers, winning_numbers):
    count1 = count_matching_numbers(numbers, winning_numbers[:-1])
    count2 = count_matching_numbers(numbers, [winning_numbers[-1]])

    if count1 == 6:
        return 1000000000
    elif count1 == 5 and count2 == 1:
        return 50000000
    elif count1 == 5 and count2 == 0:
        return 1000000
    elif count1 == 4:
        return 50000
    elif count1 == 3:
        return 5000
    else:
        return False


print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))