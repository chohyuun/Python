#4 한국 나이를 미국 나이로 변환하는 프로그램

ko_age = int(input('korea age : '))

birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))
if birth == 0 :
    us_age = ko_age
if birth < 0 :
    us_age = ko_age - 1

print('us_age : ' + str(us_age))