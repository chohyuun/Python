def make_comma(num):
    # 받은 숫자를 문자열로 전환(문자열의 순서를 반대로)
    int_to_str = str(num)[::-1]
    new_str = ''

    length = len(int_to_str) # 문자열의 길이
    comma = 0 #comma가 몇 개인지 저장

    for count in range(1, length):
        # 3번째 자리마다 콤마(,)를 입력
        if count % 3 == 0:
            # 콤마를 입력하기 위해 원래 문자를 나누고 콤마를 입력& 반복
            # EX) 1번째 자리부터 2번째까지, 3번째부터 5번째까지...
            new_str += int_to_str[count-3:count] + ','
            comma += 1

        # 콤마를 찍고 남은 부분을 입력
        # 콤마 개수보다 count가 크고 length는 콤마+1보다 작아야 한다.
        if (comma+1)*3 >= length and count >= (comma*3):
            new_str += int_to_str[count]

    # 반전으로 저장된 문자열을 재배치
    return new_str[::-1]


user = int(input("수를 입력하세요 : "))
print(make_comma(user))