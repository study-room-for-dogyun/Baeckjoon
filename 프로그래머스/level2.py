import math

def tozero(list):
    index = 0

    for i in range(len(list)):
        if list[i] != 0:
            return index
        else:
            index += 1

    return index

def solution(progresses, speeds):
    answer = []

    cnt = [0] * len(progresses)

    # 각 기능 별 완료까지 일수 계산
    for i in range(len(speeds)):
        cnt[i] = math.ceil((100 - progresses[i]) / speeds[i])


    check = [0] * len(cnt)


    for i in range(len(cnt)):
        tmp = cnt[i]

        for j in range(len(cnt)):
            cnt[j] -= tmp
            if cnt[j] < 0:
                cnt[j] = 0


        print(cnt, check)
        temp = 0
        for i in range(len(cnt[:tozero(cnt)])):
            if cnt[i] == 0 and check[i] == 0:
                temp += 1

        if temp > 0:
            answer.append(temp)

        for i in range(tozero(cnt)):
            check[i] = 1



        print(answer)

    return answer