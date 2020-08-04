import sys
sys.stdin = open('input_data/4831.txt',"r")

T = int(input())
for t in range(1, T+1):
    can_move, total_station, charge_station = list(map(int, input() .split()))
    charge_list = list(map(int, input() .split()))
    can_charge_list = []
    charge_count = 0
    start = 0
    while start + can_move < total_station :
        can_charge_list = []
        for num in range(start+1, start+ can_move+1):
            if num in charge_list:
                 can_charge_list.append(num)
        charge_count += 1
        if can_charge_list == []:
            charge_count = 0
            break
        start = max(can_charge_list)
    print('#{} {}'.format(t, charge_count))
                
