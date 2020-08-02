import sys
sys.stdin = open('input_data/1970.txt',"r")

T = int(input())
money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for t in range(1, T+1):
    print('#{}'.format(t))
    change_list = []
    money = int(input())
    for change in money_list:
        if money >= change:
            change_list.append(money//change)
            money -= change * (money//change)
        else:
            change_list.append(0)
    print(' '.join(map(str, change_list)))

















    # print('#{} {}'.format(t, new_numbers))
