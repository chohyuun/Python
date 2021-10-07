import operator


# 점수를 계산하는 함수
def total_grade(stud, ans):
    grade = 0
    for i in range(len(ans)):
        if stud[i] == ans[i]:
            grade += 10
    return grade


student = ["김갑,3242524215",
           "이을,3242524223",
           "박병,2242554131",
           "최정,4245242315",
           "정무,3242524315"]

answer = [3, 2, 4, 2, 5, 2, 4, 3, 1, 2]
num = 0

student_answer = {}
student_grade = {}

# 리스트를 사전 형태로 전환
for n in student:
    student_answer[n.split(',')[0]] = total_grade(list(map(int, n.split(',')[1])), answer)

# 점수순으로 나열하여 출력
for i in sorted(student_answer.items(), key=lambda x: x[1], reverse=True):
    num += 1
    print("학생: {} 점수: {}점 {}등".format(i[0], i[1], num))