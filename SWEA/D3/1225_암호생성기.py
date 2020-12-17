import sys; sys.stdin = open('input_data/1225.txt')
from collections import deque

keep_going = True
while keep_going:
    try:
        t = int(input())
        numbers = list(map(int, input().split()))
        numbers = [i - (min(numbers)//15 - 1) * 15  for i in numbers]
        condition = True
        cycle = 1
        while condition:
            now_num = numbers.pop(0)
            now_num -= cycle
            if now_num <= 0:
                numbers.append(0)
                condition = False
            else:
                numbers.append(now_num)
                if cycle == 5:
                    cycle = 1
                else:
                    cycle += 1
        print('#{} {}'.format(t, ' '.join(map(str, numbers))))
    except:
        keep_going = False



