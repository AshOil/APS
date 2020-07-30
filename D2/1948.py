
import sys
sys.stdin = open('input_data/1948.txt',"r")

calendar = {
        '1':31, '2':28,
        '3':31, '4':30,
        '5':31, '6':30,
        '7':31, '8':31,
        '9':30, '10':31,
        '11':30, '12':31
}

T = int(input())
for t in range(1, T+1):
    numbers = list(map(int, input() .split()))
    first_month, first_day = numbers[0], numbers[1]
    last_month, last_day = numbers[2], numbers[3]
    result = 0
    if last_month > first_month:
        for gap in range(first_month, last_month):
            result += calendar[str(gap)]
        result -= first_day
        result += last_day + 1
        print('#{} {}'.format(t,result))
    
    else:
        result += last_day - first_day +1
        print('#{} {}'.format(t,result))

    




