# ---------------------------------------------------------------
# 에러 조건
# 1. 숫자가 아닌 경우
# 2. 숫자열이 4개이상인 경우
# 3. 32 이상인 경우
# 4. 숫자가 연속되지 않는 경우
# ---------------------------------------------------------------

import random


# 컴퓨터의 선택 출력
def com_chose(end):
    com_turn = random.randint(1, 3)
    com_n = []
    for n in range(com_turn):
        if end + n > 31:
            print("나의 승리!")
            break
        com_n.append(end + n)
        print("컴퓨터 :", end + n)
    return com_n


# 에러 조건 확인
# raise 를 이용하여 강제적으로 예외 발생
# 참고 : https://dojang.io/mod/page/view.php?id=2400
def error_check(check_list, end):
    for n in check_list:
        if not n.isdigit():
            raise Exception('숫자를 입력해 주세요')

    # 리스트를 숫자로 변환시키기
    int_list = list(map(int, check_list))

    if len(int_list) >= 4:
        raise Exception('선택가능한 범위를 벗어납니다.\n숫자를 3개만 입력해 주세요\n')
    elif int_list[-1] > 31:
        raise Exception('숫자가 범위를 넘었습니다.\n32이상이 되면 안됩니다.\n')
    elif int_list != list(range(int(check_list[0]), int(check_list[-1]) + 1)):
        raise Exception('연속된 숫자열이 아닙니다.\n')
    elif int(int_list[0]) != end:
        raise Exception('시작 숫자가 틀렸습니다.\n')


end_num = 1 # 마지막으로 입력된 숫자 저장

while end_num != -1:
    my = []
    com = []
    try:
        my = input("My turn - 숫자를 입력하세요: ")
        my = my.split()
        error_check(my, end_num)
        print("현재 숫자 :", my[-1])

        if int(my[-1]) == 31:
            print("컴퓨터의 승리!")
            break

        end_num = int(my[-1]) + 1

        com += com_chose(end_num)
        print("현재 숫자 :", com[-1])

        if end_num == 31:
            break

        end_num = com[-1] + 1

    except Exception as err:
        print(err)