import sys

sys.stdin = open('input_data/1974.txt',"r")
num_dict = {}
T = int(input())

for t in range(1, T+1):
    for tt in range(1,10):
        num_dict[tt] = list(map(int, input() .split()))
    result = True

    # 가로부터 검사하자
    for hori in num_dict.values():
        if sorted(hori) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            result = False

    #세로 검사
    for num in range(9):
        verti_check = []
        for verti in num_dict.values():
            verti_check.append(verti[num])
            verti_result = verti_check
        if sorted(verti_check) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            result = False


    #블록검사
    line_start = 0
    line_end = 3
    block_list = list(num_dict.values())
    for __ in range(3):
        turn_block_list = block_list[line_start:line_end]
        block_start = 0
        block_end = 3
        for _ in range(3):
            block_check = []
            for turn in range(3):
                for block in turn_block_list[turn][block_start:block_end]:
                    block_check.append(block)
            block_start += 3
            block_end += 3
            if sorted(block_check) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                result = False
        line_start += 3
        line_end += 3

    if result:
        print('#{} 1'.format(t))
    else:
        print('#{} 0'.format(t))






        
