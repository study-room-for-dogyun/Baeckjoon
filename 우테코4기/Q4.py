# 문제 설명
# 처음과 끝이 이어져 있는 문자열을 상상해봅시다. 당신은 해당 문자열 내의 "같은 글자가 연속해 있는" 구간들을 추출하고자 합니다.
#
# 문자열 s가 매개변수로 주어집니다. s 내의 모든 "같은 글자가 연속해 있는" 구간의 길이를 각각 배열에 담아 오름차순으로 정렬하여 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 3 ≤ s의 길이 ≤ 1,000
# s는 영어 소문자로 이루어진 문자열입니다.
# 입출력 예
# s	result
# "aaabbaaa"	[2,6]
# "wowwow"	[1,1,2,2]

def solution(s):
    answer = []

    cnt = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)

    if s[0] == s[-1]:
        answer[0] += answer[-1]
        answer = answer[:-1]

    if not answer:
        answer.append(len(s))

    answer.sort()

    return answer