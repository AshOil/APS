import sys
sys.stdin = open('input_data/1268.txt',"r")

student_num = int(input())
student_classes= []
for _ in range(student_num):
    student_classes.append(list(map(int,input().split())))
