import sys
sys.stdin = open('input_data/1206.txt',"r")

for t in range(1,11):
    tower_count = int(input())
    towers = list(map(int, input() .split()))
    result = 0
    for number in range(2, tower_count-2):
        second_tower = sorted(towers[number-2:number+3])[3]
        if towers[number] == max(towers[number-2:number+3]):
            count = towers[number] - second_tower
            result += count
    print('#{} {}'.format(t,result))
            