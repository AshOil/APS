import sys; sys.stdin = open('input_data/5208.txt')

def findBattery(i, count):
    global min_charge
    if count > min_charge: return
    if i + battery[i] >= end:
        if count < min_charge:
            min_charge = count
    for j in range(i+1, i + battery[i] + 1):
        findBattery(j, count + 1)

for t in range(1, int(input()) + 1):
    battery = list(map(int,input().split()))
    end = battery.pop(0) - 1
    min_charge = 100
    findBattery(0, 0)
    print('#{} {}'.format(t, min_charge))