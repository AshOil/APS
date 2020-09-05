import sys
sys.stdin = open('input_data/2028.txt',"r")

# data 받아오기
T = int(input())
for _ in range(T):
    number = int(input())
    # 뒤에서 몇개의 숫자를 봐야하는지 확인하기 위해 len구하기
    length_num = len(str(number))
    double = number ** 2
    length_dou = len(str(double))
    # 슬라이싱을 하기위해 str로 만들고 비교
    if str(double)[length_dou-length_num::] == str(number):
        print('YES')
    else: print('NO')