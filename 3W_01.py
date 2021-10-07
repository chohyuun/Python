# 구구단 함수
def gugudan(number):
    i = 1

    # i가 10보다 작을 때까지 반복
    while i < 10:
        print("{} X {} = {}".format(number, i, number*i))
        i += 1


number = int(input("몇 단? : "))
gugudan(number)