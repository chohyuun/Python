def check_numbers(text):
    save = open('number.txt', 'w', encoding="UTF-8")
    save.write(text)
    save.close()

    name = []
    error = []

    # 파일 읽을때 인코딩 방식 변경
    num_file = open('number.txt', 'r', encoding='UTF8')

    for line in num_file:
        # 방명록을 리스트로 저장(조건 : ,과 ' '를 기준으로 자르기
        # 2차원 배열로 저장된다
        name.append(line.strip().split(','))

    for count in name:
        # 길이가 13보다 짧거나 길 경우'-' 포함
        if len(count[1]) != 13:
            error.append(count)
        # 번호가 010으로 시작하지 않는 경우
        elif count[1][:3] != '010':
            error.append(count)
        # 번호 중간중간 들어가야 할 자리에 '-'가 들어가지 않은 경우
        elif count[1][3] != '-' and count[1][8] != '-':
            error.append(count)

    for count in error:
        print("잘못 쓴 사람: ", count[0])
        print("잘못 쓴 번호: ", count[1], '\n')


text = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""

check_numbers(text)