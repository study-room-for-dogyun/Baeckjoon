# 문제 설명
# 해외 여행을 매우 좋아하는 준이 다니고 있는 대표적인 푸드테크 기업 W는 주 35시간 근무, 시간제 휴가로 유명한 회사입니다. 준은 회사의 출퇴근 시간을 잘 활용하여 해외 여행은 항상 금요일에 출발하여 다음 월요일에 돌아오도록 여행 일정을 세웁니다.
#
# 요일	출근 시간	퇴근 시간
# 월	1PM	6PM
# 금	9:30AM	6PM
# 올해 호치민을 마지막으로 다녀온 준은 남은 휴가 시간을 고려하지 않은 채 비행기 시간만 고려하여 여행 일정을 세웠습니다. 올해 남은 휴가 시간 time과 여행 일정을 담은 이차원 배열 plans가 매개변수로 주어질 때, 남은 휴가 시간 내에 갈 수 있는 여행지 중 준의 올해 마지막 여행지가 어디인지 return 하도록 solution 메서드를 완성해주세요.
#
# 제한사항
# 1 ≤ plans의 길이 ≤ 1,000
# plans의 원소는 여행지, 출발 시간, 도착 시간 형식입니다.
# 여행 일정은 겹치지 않으며 계획 순서대로 이루어져 있습니다.
# 여행지는 길이가 1 이상 30 이하인 문자열입니다.
# 출발 시간과 도착 시간은 12시간제로 표기하며 길이가 3 이상 4 이하인 문자열입니다.
# 출발 시간과 도착 시간의 최소 단위는 1시간입니다.
# 출발 시간은 금요일이 기준이며, 도착 시간은 다음 월요일이 기준입니다.
# 오전은 "AM", 오후는 "PM"으로 표기합니다.
# time의 0.5는 30분을 의미하며, time의 최소 단위는 30분입니다.
# 회사에서 공항까지 이동 시간, 점심시간은 고려하지 않습니다.
# 입출력 예
# time	plans	result
# 3.5	[ ["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"] ]	"홍콩"
# 입출력 예 설명
# 입출력 예 1
# 올해 남은 휴가 시간은 3.5시간입니다. 엘에이까지 다녀오려면 4시간의 휴가가 필요해서 30분이 부족합니다. 따라서 마지막 여행지는 홍콩입니다.

def change_to_24(t):
    time = 0
    until = 0
    if 'P' in t:
        until = t.index('P')
        t = t[:until].split(':')
        if len(t) == 1:
            time = int(t[0]) + 12
        else:
            time = int(t[0]) + float(int(t[1]) / 60) + 12

    elif 'A' in t:
        until = t.index('A')
        t = t[:until].split(':')
        if len(t) == 1:
            time = int(t[0])
        else:
            time = int(t[0]) + float(int(t[1]) / 60)

    return time


def solution(time, plans):
    answer = ''

    monday = 13
    friday = 18

    for idx, i in enumerate(plans):
        place, start, end = i
        start = change_to_24(start)
        end = change_to_24(end)

        if start < friday:
            time -= min(8.5, friday - start)

        if end > monday:
            time -= min(5, end - monday)

        if time < 0:
            if idx == 0:
                answer = '호치민'
            else:
                answer = plans[idx - 1][0]
            break

    return answer