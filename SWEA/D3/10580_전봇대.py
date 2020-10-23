### 푸는중

import sys; sys.stdin = open('input_data/10580.txt')

for t in range(1, int(input())+1):
    number = int(input())
    lines = [list(map(int, input().split())) for _ in range(number)]
    result = 0
    for standard_line in lines:
        for check_line in lines:
            st_left = standard_line[0]
            st_right = standard_line[1]
            ch_left = check_line[0]
            ch_right = check_line[1]
            st_degree = st_right - st_left
            ch_degree = ch_right - ch_left
            if st_degree == ch_degree : continue
            # st : +, ch : +

