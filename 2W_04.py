def bus_fare(age, payment) :
    print("나이: {}세".format(age))
    print("지불유형: {}".format(payment))


    if age <= 7 or age >= 75:
        fare = '무료'
    elif age >= 8 and age <= 13 :
        fare = '450원'
    elif age >= 14 and age <= 19 :
        if payment == '현금' :
            fare = '1000원'
        else :
            fare = '750원'
    elif age >= 20 and age <= 74 :
        if payment == '현금' :
            fare = '1300원'
        else :
            fare = '1200원'

    print("버스 요금: {}".format(fare))


age = int(input())
payment = input()

bus_fare(age, payment)
