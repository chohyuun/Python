def grader(name, score) :
    if score < 60 :
        grade = 'F'
    elif score >= 60 and score <= 64 :
        grade = 'D'
    elif score >= 65 and score <= 69 :
        grade = 'D+'
    elif score >= 70 and score <= 74 :
        grade = 'C'
    elif score >= 75 and score <= 79 :
        grade = 'C+'
    elif score >= 80 and score <= 84 :
        grade = 'B'
    elif score >= 85 and score <= 89 :
        grade = 'B+'
    elif score >= 90 and score <= 94 :
        grade = 'A'
    else :
        grade = 'A+'

    print("학생 이름 : {} \n점수 : {} \n학점 : {}".format(name, score, grade))


student_name = input()
student_grade = int(input())

grader(student_name, student_grade)
