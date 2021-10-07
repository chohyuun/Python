import operator # 정렬을 위해 사용
import statistics # 평균값을 구하기 위해 사용
import math # 버림 할 때 사용

records_aver = {}


def sales_management(member_name, member_records):
    records_aver = aver_dict(member_name, member_records)
    for n in range(len(member_records)):
        if 0 <= n < 2: # 순위가 1, 2위일 때
            if records_aver[n][1] > 4: # 점수 평균이 4보다 크면 보너스 대상
                print("보너스 대상자 ", records_aver[n][0])
        elif 4 < n < 7: # 순위가 5, 6위일 때
            if records_aver[n][1] < 4: # 점수 평균이 4점보다 낮으면 면담 대상
                print("면담 대상자", records_aver[n][0])


# 받은 두개의 배열을 사전으로 변환
# 그리고 점수를 평균으로 변환하고 소숫점 이하를 버림한다
def aver_dict(member_name, member_records):
    for n in range(len(member_records)):
        # math.floor : 버림용 함수
        # statistics.mean : 평균값을 반환하는 함수
        records_aver[member_name[n]] = math.floor(statistics.mean(member_records[n]))

    # sorted : 정렬 sorted(정렬하고자 하는것, 정렬 기준으로 잡을 것, reverse: 역순으로 할지 결정)
    # 참고 : https://wikidocs.net/109327 정렬 기준으로 잡는 부분(operator.itemgetter())에 대한 참고 자료
    return sorted(records_aver.items(), key=operator.itemgetter(1), reverse=True)


member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4, 5, 3, 5, 6, 5, 3, 4, 1, 3, 4, 5], [2, 3, 4, 3, 1, 2, 0, 3, 2, 5, 7, 2],
                  [1, 3, 0, 3, 3, 4, 5, 6, 7, 2, 2, 1], [3, 2, 9, 2, 3, 5, 6, 6, 4, 6, 9, 9],
                  [8, 7, 7, 5, 6, 7, 5, 8, 8, 6, 10, 9], [7, 8, 4, 9, 5, 10, 3, 3, 2, 2, 1, 3]]

sales_management(member_names, member_records)
