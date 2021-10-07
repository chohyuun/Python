def yearly_payment(m_payment) : #세후 연봉 계산
    if m_payment <= 1200 :
        y_payment = m_payment * 0.94
    elif m_payment <= 4600 :
        y_payment = m_payment * 0.85
    elif m_payment <= 8800 :
        y_payment = m_payment * 0.76
    elif m_payment <= 15000 :
        y_payment = m_payment * 0.65
    elif m_payment <= 30000 :
        y_payment = m_payment * 0.62
    elif m_payment <= 50000 :
        y_payment = m_payment * 0.60
    else :
        y_payment = m_payment * 0.58
    return y_payment


monthly_payment = int(input())

print("세전 연봉 : {}만원".format(monthly_payment * 12))
print("세후 연봉 : {:.0f}만원".format(yearly_payment(monthly_payment * 12)))
