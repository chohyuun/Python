# 소수 출력
def count_prime_number(n, m):
    count = 0
    result = 0
    numbers = [i for i in range(n, m+1)]

    while count < len(numbers):
        if numbers[count] > 3:
            if numbers[count]%2 != 0 and numbers[count]%3 != 0:
                result += 1
        else:
            result += 1

        count += 1

    print("소수의 개수 : {}".format(result))


try:
    n = int(input("첫 번째 수 입력: "))
    m = int(input("두 번째 수 입력: "))

    count_prime_number(n, m)

except:
    print("입력을 다시 해주세요.")