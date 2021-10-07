import operator


def stock_profit(stocks, sells):
    stock_dict = {}
    stock = []

    # stocks 안의 내용을 필요에 맞게 나누기
    for n in stocks.split(','):
        stock.append(n.split('/'))

    # 수익률 계산: (현재가/평균단가)*100 - 100
    for n in range(len(sells)):
        # 키 : 회사의 이름
        # 값 : 수익률
        stock_dict[stock[n][0]] = (((int(sells[n])/int(stock[n][2]))*100)-100)

    # 사전을 정렬(값을 기준으로)
    stock_dict = sorted(stock_dict.items(), key=operator.itemgetter(1), reverse=True)

    for n in stock_dict:
        # 정렬한 내용을 출력(수익률은 소수점 2자리까지 출력)
        print(f"{n[0]}의 수익률 {n[1]:.3}")


stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]
stock_profit(stocks, sells)