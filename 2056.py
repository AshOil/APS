import sys

sys.stdin = open('input_data/2056.txt')


def check_month(month):
    if 0 <int(month) < 13:
        return month
    return ''

def check_day(month, day):
    day_dict = {
        '01':31, '02':28,
        '03':31, '04':30,
        '05':31, '06':30,
        '07':31, '08':31,
        '09':30, '10':31,
        '11':30, '12':31
        }
    if 0 < int(day) < 32:
        if int(day) <= day_dict.get(month):
            return day 
        return ''

# '5' ==> 5
T = int(input())

# 1,2,3,4,5
for t in range(1,T+1):
    target = input()
    year, month, day = target[:4], target[4:6], target[6:]

    month = check_month(month)
    day = check_day(month, day)
    
    if month and day:
        print('#{} {}/{}/{}'.format(t, year, month, day))
    else:
        print('#{} -1'.format(t))
