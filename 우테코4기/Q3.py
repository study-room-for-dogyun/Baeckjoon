

# 문제
# 설명
# 음식점에서
# 하루
# 동안의
# 판매
# 수익을
# 계산하고자
# 합니다.아래
# 3
# 개의
# 표는
# 각각
# 음식점에서
# 사용하는
# 재료, 판매하는
# 메뉴, 하루
# 동안의
# 판매
# 실적에
# 대한
# 정보를
# 나타내는
# 예시입니다.
#
# 재료의
# 정보
#
# 재료
# 이름
# 가격(원)
# r
# 10
# a
# 23
# t
# 124
# k
# 9
# 음식점에서는
# 메뉴를
# 만들기
# 위해
# 재료를
# 구매해옵니다.재료
# r의
# 구매
# 비용은
# 10
# 원, 재료
# a의
# 구매
# 비용은
# 23
# 원, 재료
# t의
# 구매
# 비용은
# 124
# 원, 재료
# k의
# 구매
# 비용은
# 9
# 원입니다.
#
# 메뉴의
# 정보
#
# 메뉴
# 이름
# 필요한
# 재료
# 판매가(원)
# PIZZA
# arraak
# 145
# HAMBURGER
# tkar
# 180
# BREAD
# kkk
# 30
# ICECREAM
# rar
# 50
# SHAVEDICE
# rar
# 45
# JUICE
# rra
# 55
# WATER
# a
# 20
# 필요한
# 재료에
# 포함된
# 알파벳의
# 개수는
# 해당
# 메뉴를
# 만들
# 때
# 필요한
# 재료의
# 수입니다.
# 음식점에서
# PIZZA를
# 만들기
# 위해서
# 6
# 개의
# 재료(a는
# 3
# 개, r은
# 2
# 개, k는
# 1
# 개)가
# 필요하므로, 총
# 재료비는
# 69 + 20 + 9 = 98
# 입니다.
# a: 3
# 개 → 23
# x
# 3 = 69
# r: 2
# 개 → 10
# x
# 2 = 20
# k: 1
# 개 → 9
# x
# 1 = 9
# PIZZA를
# 1
# 개
# 판매하면
# 얻을
# 수
# 있는
# 수익은
# 다음과
# 같습니다.
# 145(판매가) - 98(재료비) = 47(수익)
# ICECREAM, SHAVEDICE, JUICE는
# 모두
# 똑같은
# 재료(r은
# 2
# 개, a는
# 1
# 개)를
# 사용하므로
# 재료비는
# 같으나, 판매가가
# 다르므로
# 판매
# 시
# 얻을
# 수
# 있는
# 수익은
# 다릅니다.
# WATER처럼
# 판매하면
# 수익이
# 아닌, 손실이
# 발생하는
# 메뉴도
# 있을
# 수
# 있습니다.
# 20(판매가) - 23(재료비) = -3
#
# 하루
# 동안의
# 판매
# 실적
#
# 메뉴
# 이름
# 판매
# 수량
# BREAD
# 5
# ICECREAM
# 100
# PIZZA
# 7
# JUICE
# 10
# WATER
# 1
# BREAD
# 5
# 개를
# 판매해서
# 얻은
# 수익: (30 - 27)
# x
# 5 = 15
# ICECREAM
# 100
# 개를
# 판매해서
# 얻은
# 수익: (50 - 43)
# x
# 100 = 700
# PIZZA
# 7
# 개를
# 판매해서
# 얻은
# 수익: (145 - 98)
# x
# 7 = 329
# JUICE
# 10
# 개를
# 판매해서
# 얻은
# 수익: (55 - 43)
# x
# 10 = 120
# WATER
# 1
# 개를
# 판매해서
# 얻은
# 수익: (20 - 23)
# x
# 1 = -3
# 따라서, 하루
# 동안의
# 총수익은
# 15 + 700 + 329 + 120 - 3 = 1161
# 입니다.
# 재료
# 정보를
# 담은
# 문자열
# 배열
# ings, 메뉴
# 정보를
# 담은
# 문자열
# 배열
# menu, 하루
# 동안의
# 판매
# 실적을
# 담은
# 문자열
# 배열
# sell이
# 매개변수로
# 주어집니다.이때, 하루
# 동안의
# 총수익을
# return 하도록
# solution
# 함수를
# 완성해주세요.
# 총수익은
# 음수가
# 될
# 수도
# 있습니다.(입출력
# 예  # 2 참고)
#
# 제한사항
# 1 ≤ ings의
# 길이 ≤ 26
# ings의
# 각
# 원소는
# "ING_NAME ING_PRICE"
# 형식입니다.
#     ING_NAME은
# 재료의
# 이름을
# 나타내며, 알파벳
# 소문자
# 하나로
# 표시됩니다.
#     ING_PRICE는
# 재료의
# 가격을
# 나타내는
# 정수입니다.
# 1 ≤ ING_PRICE ≤ 1000
# ING_NAME과
# ING_PRICE는
# 1
# 개의
# 공백으로
# 구분되어
# 있습니다.
#     ings에서
# ING_NAME은
# 중복되어
# 나타나지
# 않습니다.
# 1 ≤ menu의
# 길이 ≤ 100
# menu의
# 각
# 원소는
# "MENU_NAME ING_LIST MENU_PRICE"
# 형식입니다.
#     MENU_NAME은
# 식당에서
# 판매하고
# 있는
# 메뉴의
# 이름을
# 나타내며, 알파벳
# 대문자로
# 구성된
# 문자열입니다.
# 3 ≤ MENU_NAME의
# 길이 ≤ 10
# ING_LIST는
# 메뉴를
# 만드는데
# 필요한
# 재료들을
# 나타내는, 알파벳
# 소문자로
# 구성된
# 문자열입니다.
# 1 ≤ ING_LIST의
# 길이 ≤ 20
# ings에
# 담겨있는
# 재료들만
# ING_LIST에
# 나타납니다.
#     MENU_PRICE는
# 메뉴의
# 가격을
# 나타내는
# 정수입니다.
# 1 ≤ MENU_PRICE ≤ 20000
# MENU_NAME, ING_LIST, MENU_PRICE는
# 1
# 개의
# 공백으로
# 구분되어
# 있습니다.
#     menu에서
# MENU_NAME은
# 중복되어
# 나타나지
# 않습니다.
# 1 ≤ sell의
# 길이 ≤ menu의
# 길이 ≤ 100
# sell의
# 각
# 원소는
# "MENU_NAME SELL_COUNT"
# 형식입니다.
#     MENU_NAME은
# 판매된
# 메뉴의
# 이름을
# 나타내며, 알파벳
# 대문자로
# 구성된
# 문자열입니다.
# 3 ≤ MENU_NAME의
# 길이 ≤ 10
# menu의
# MENU_NAME으로
# 나타난
# 것들만
# sell의
# MENU_NAME에
# 나타납니다.
#     SELL_COUNT는
# 메뉴가
# 판매된
# 수량입니다.
# 1 ≤ SELL_COUNT ≤ 100
# MENU_NAME과
# SELL_COUNT는
# 1
# 개의
# 공백으로
# 구분되어
# 있습니다.
#     sell에서
# MENU_NAME은
# 중복되어
# 나타나지
# 않습니다.
#     입출력
# 예
# ings
# menu
# sell
# result
# ["r 10", "a 23", "t 124", "k 9"][
#     "PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"][
#     "BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]
# 1161
# ["x 25", "y 20", "z 1000"]["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"]["BBBB 3", "TTT 2"] - 80
# 입출력
# 예
# 설명
# 입출력
# 예  # 1
#
# 문제
# 예시와
# 같습니다.
#
#     입출력
# 예  # 2
#
# 재료의
# 정보
#
# 재료
# 이름
# 가격(원)
# x
# 25
# y
# 20
# z
# 1000
#
# 메뉴의
# 정보
#
# 메뉴
# 이름
# 필요한
# 재료
# 판매가(원)
# AAAA
# xyxy
# 15
# TTT
# yy
# 30
# BBBB
# xx
# 30
#
# 하루
# 동안의
# 판매
# 실적
#
# 메뉴
# 이름
# 판매
# 수량
# BBBB
# 3
# TTT
# 2
# BBBB
# 3
# 개를
# 판매해서
# 얻은
# 수익: (-20)
# x
# 3 = -60
# TTT
# 2
# 개를
# 판매해서
# 얻은
# 수익: (-10)
# x
# 2 = -20
# 따라서, 하루
# 동안의
# 총수익은(-60) + (-20) = -80
# 입니다.

def solution(ings, menu, sell):
    answer = 0

    # 재료 가격 저장
    ings_price = {}
    for i in ings:
        temp = i.split(' ')
        ings_price[temp[0]] = int(temp[1])

    # 메뉴 가격 저장
    menu_price = {}
    for i in menu:
        temp = i.split(' ')
        price = 0
        for ing in temp[1]:
            price += ings_price[ing]
        menu_price[temp[0]] = [price, int(temp[2])]

    # 판매 실적으로 수익 계산
    for i in sell:
        temp = i.split(' ')
        count = int(temp[1])
        make_price, sell_price = menu_price[temp[0]]
        answer += (sell_price - make_price) * count

    return answer