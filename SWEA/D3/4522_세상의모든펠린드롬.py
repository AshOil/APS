import sys
sys.stdin = open('input_data/4522.txt')

def Change(number, i):
    new_number = ''
    for idx, num in enumerate(number):
        if idx < i :
            new_number += num
        else:
            if num == '0':
                new_number += '1'
            else: new_number += '0'
    return new_number

T = int(input())
for t in range(1,T+1):
    number = input()
    length = len(number)
    now = '0'*length
    count = 0
    for i in range(length):
        if not now[i] == number[i]:
            now = Change(now, i)
            count += 1
    print('#{} {}'.format(t, count))




