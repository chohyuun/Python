# 가위 바위 보
import random

def rsp_advanced(games):
    count = 0 # 횟수를 확인 하기 위한 변수
    # 리스트를 이용한 선택지 문자 출력
    choice = ["가위", "바위", "보"] 

    while count < games: # 선택한 횟 수 만큼 반복
        computers_choice = random.randint(0, 2)
        my_choice = input("가위 바위 보: ")

        my_choice_int = int(str_to_int(my_choice))

        # 0에서 2사이의 값일 경우 출력
        if 0 <= my_choice_int <= 2:
            print("나: {}".format(choice[my_choice_int]))
            print("컴퓨터: {}".format(choice[computers_choice]))

            result = print_result(computers_choice, my_choice_int)

            if result == 0:
                print("{}번째 판 비겼습니다.".format(count + 1))
            elif result == 1:
                print("{}번째 판 내 승리!".format(count + 1))
            else:
                print("{}번째 판 컴퓨터 승리".format(count + 1))

            count += 1
        
        # 0에서 2사이가 아닌 경우 문자를 출력 // 횟수는 증가 하지 않고 계속 반복
        else:
            print("틀린 입력\n다시 입력하세요.\n")


# 문자일 경우의 출력 변경
def str_to_int(my_choice):
    try: 
        if 0 <= int(my_choice) <= 2:
            return my_choice
        else: # 숫자가 범위 내가 아닐 경우 3을 반환
            return 3

    # 숫자가 아닐 때 문자인지 확인
    except:
        if my_choice == "가위":
            return 0
        elif my_choice == "바위":
            return 1
        elif my_choice == "보":
            return 2
        else:
            return 3


# 가위 바위 보 결과 출력
def print_result(computer, me):
    result = computer - me

    if result == 0:
        return 0
    elif result == -1 or result == 2:
        return 1
    else:
        return 2


games = int(input("몇 판을 진행하시겠습니까? : "))
rsp_advanced(games)
