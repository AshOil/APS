import sys
sys.stdin = open('input_data/2851.txt',"r")

vacancy = [0] * 10
vacancy[0] = int(input()) -100
for i in range(1,10):
    vacancy[i] = vacancy[i-1] + int(input())
max_num = -1000
min_num =  1000
if 0 in vacancy:
    print(100)
else:
    for van in vacancy:
        if van < 0:
            if van > max_num:
                max_num = van
        else:
            if van < min_num:
                min_num = van
    if abs(min_num) == abs(max_num):
        print(min_num+100)
    elif abs(min_num) > abs(max_num):
        print(max_num+ 100)
    else: print(min_num + 100)


