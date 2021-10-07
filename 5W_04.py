import datetime # 일자 모듈 import 

# 요일 출력
week = ['월', '화', '수', '목', '금', '토', '일']

while True:
    insert_date = input("연도 부터 입력(ex. 2021 08 14/ -1을 입력하면 종료): ")
    if insert_date == '-1':
        break
        
    # 날짜가 들어오면 년, 월, 일로 변환
    insert_date = insert_date.split()

    year = int(insert_date[0])
    month = int(insert_date[1])
    day = int(insert_date[2])

    # Python이 이해할 수 있는 날짜의 형태로 변환
    date = datetime.datetime(year, month, day)

    # 100일 후를 계산
    before_100_date = date + datetime.timedelta(days=100)
    print("{}년 {}월 {}일".format(before_100_date.year, before_100_date.month, before_100_date.day), week[before_100_date.weekday()], "요일")