import sys; sys.stdin = open('input_data/4047.txt')

for t in range(1, int(input()) + 1):
    card_data = input()
    cards = len(card_data)//3
    if cards > 52:
        print('#{} ERROR'.format(t))
        continue
    S = [0] * 14
    D = [0] * 14
    H = [0] * 14
    C = [0] * 14
    S_num = 13
    D_num = 13
    H_num = 13
    C_num = 13
    for i in range(0, len(card_data), 3):
        if card_data[i] == 'S':
            if S[int(card_data[i+1: i+3])]:
                print('#{} ERROR'.format(t))
                break
            else:
                S[int(card_data[i+1: i+3])] = 1
                S_num -= 1
        elif card_data[i] == 'D':
            if D[int(card_data[i+1: i+3])]:
                print('#{} ERROR'.format(t))
                break
            else:
                D[int(card_data[i+1: i+3])] = 1
                D_num -= 1
        elif card_data[i] == 'H':
            if H[int(card_data[i+1: i+3])]:
                print('#{} ERROR'.format(t))
                break
            else:
                H[int(card_data[i+1: i+3])] = 1
                H_num -= 1
        else:
            if C[int(card_data[i+1: i+3])]:
                print('#{} ERROR'.format(t))
                break
            else:
                C[int(card_data[i+1: i+3])] = 1
                C_num -= 1
    else:
        print('#{} {} {} {} {}'.format(t, S_num, D_num, H_num, C_num))
