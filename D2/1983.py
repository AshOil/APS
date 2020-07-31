import sys
import math
sys.stdin = open('input_data/1983.txt',"r")
grade_chart = {
    '1' : 'A+', '2' : 'A0',
    '3' : 'A-', '4' : 'B+',
    '5' : 'B0', '6' : 'B-',
    '7' : 'C+', '8' : 'C0',
    '9' : 'C-', '10' : 'D0'
}

T = int(input())
for t in range(1, T+1):
    student_num, who_we_want = list(map(int, input() .split()))
    students_grade = []
    that_grade = 0
    for number in range(1, student_num+1):
        grade_list = list(map(int, input() .split()))
        real_grade =(((35 * grade_list[0]) + (45 * grade_list[1]) + (20 * grade_list[2])) / 100)
        students_grade.append(real_grade)
        if number == who_we_want:
            that_grade += real_grade
    students_grade.sort(reverse=True)
    adjust = (student_num/10)
    count = 1
    for in_grade in students_grade:
        if in_grade == that_grade:
            get_grade = str(grade_chart[str(math.ceil(count/adjust))])
            print('#{} {}'.format(t, get_grade))
        else:
            count += 1
    



