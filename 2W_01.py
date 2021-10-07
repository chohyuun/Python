def rcy(my) : # 가위바위보의 결과 출력
    import random
    computer = random.randint(0, 2)
    result = computer - my

    if result == 0 :
        print("나 : {}".format(print_choice(my)))
        print("컴퓨터 : {}".format(print_choice(computer)))
        print("비겼습니다.")
    elif result == -1 or result == 2 :
        print("나 : {}".format(print_choice(my)))
        print("컴퓨터 : {}".format(print_choice(computer)))
        print("내 승리!")
    elif result == -2 or result == 1 :
        print("나 : {}".format(print_choice(my)))
        print("컴퓨터 : {}".format(print_choice(computer)))
        print("컴퓨터 승리!")

def print_choice(ch) : #가위바위보 중 선택한 것을 문자열로 반환
    if ch == 0 :
        return "가위"
    elif ch == 1 :
        return "바위"
    elif ch == 2 :
        return "보"


my_str = input()

if my_str == '가위' :
    my = 0
elif my_str == '바위' :
    my = 1
elif my_str == '보' :
    my = 2
else :
    my = int(my_str)

rcy(my)
