import operator

CUT_NUM = 6

def good_customer(info):
    # 리스트 컴프리헨션
    # [(실제 할당 값) for (사용할 변수 이름) in (범위 조건)]
    # 참고 : https://shoark7.github.io/programming/python/about-list-comprehension-python
    cut_info = [info[i * CUT_NUM:(i + 1) * CUT_NUM] for i in range((len(info) + CUT_NUM - 1) // CUT_NUM)]
    detail_info = {'아이디': [], '나이': [], '전화번호': [], '성별': [], '지역': [], '구매횟수': []}
    dict_key = list(detail_info.keys()) # 사전에 저장되어야 할 키들을 저장
    vip_addr = [] # vip 회원의 위치들을 저장
    vip = [] # vip 회원

    for n in range(len(cut_info)):
        info_list = []
        for i in range(CUT_NUM):
            if cut_info[i][n] == 'x':
                info_list.append('000-0000-0000')
                continue
            info_list.append(cut_info[i][n])
        detail_info[dict_key[n]] = info_list

    for n in range(CUT_NUM):
        if int(detail_info['구매횟수'][n]) > 7:
            if detail_info['전화번호'][n] != '000-0000-0000':
                vip_addr.append(n)

    print("**회원 정보 출력**")
    for key, value in detail_info.items():
        print(key, value)
        for i in vip_addr:
            vip.append(detail_info[key][i])
    print("\n\n할인 쿠폰을 받을 회원정보")
    for n in range(CUT_NUM):
        print(f"{dict_key[n]} : {vip[n]}")


info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"
good_customer(info.split(','))
