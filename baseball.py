import random

def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        temp = random.randint(0, 9)
        if temp not in numbers:
            numbers.append(temp)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.")
    return numbers

def take_guess():

    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    user = []

    while len(user) < 3:
        n = int(input(f"{len(user) + 1}번째 숫자를 입력하세요: "))
        if n in user:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            continue
        elif n > 9 or n < 0:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        else:
            user.append(n)    

    return user

def get_score(guesses, solution):
    s = 0
    b = 0

    for i in guesses:
        for j in solution:
            if i == j:
                b += 1
    
    for i in range(3):
        if guesses[i] == solution[i]:
            s += 1
    
    return s, b - s

# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    user = take_guess()
    s, b = get_score(user, ANSWER)
    print(f"{s}S {b}B")
    tries += 1
    if s == 3:
        break


print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))