def check_id(id):
    wrong = "잘못된 번호입니다.\n올바른 번호를 넣어주세요."
    while True:
        check = id.split('-')

        # 숫자만 입력했는지 확인
        try:
            int(check[0] + check[1])
        except:
            print(wrong)
            break

        # 월과 일이 범위를 넘어서지 않는지 확인
        if 0 > int(check[0][2:4]) > 13 and 0 > int(check[4:6]) > 32:
            print(wrong)
            break
        # 주민번호의 앞부분이 6자리, 뒷부분이 7자리, 중간에 '-'가 맞는지 확인
        elif len(check[0]) != 6 and len(check[1]) != 7 and id[6] != '-':
            print(wrong)
            break
        # 생년이 00~21인 경우
        elif 0 <= int(check[0][0:2]) < 22:
            birth = input("2000년 이후 출생자 입니까? 맞으면 o 아니면 x: ")

            if birth == 'o':
                # 00년생 이후 출생이면서 뒷자리가 1, 2인 경우 오류
                if 0 < int(check[1][0]) < 3:
                    print(wrong)
                    break
            else:
                # 00년생 이전 출생이면서 뒷자리가 3, 4인 경우 오류
                if 2 < int(check[1][0]) < 5:
                    print(wrong)
                    break

        # 1,3일 경우 남자
        if check[1][0] == '1' or check[1][0] == '3':
            print('{}년{}월 남자\n'.format(check[0][:2], check[0][2:4]))
        # 2,4일 경우 여자
        elif check[1][0] == '2' or check[1][0] == '4':
            print('{}년{}월 여자\n'.format(check[0][:2], check[0][2:4]))

        else:
            print(wrong)
        break


while True:
    id = input("주민번호를 입력하세요(exit: q): ")
    if id == 'q':
        print("종료됩니다.")
        break
    check_id(id)