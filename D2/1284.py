import sys
sys.stdin = open('input_data/1284.txt','r')

T = int(input())


for t in range(1, T+1):
    numbers = list(map(int, input() .split()))
    a_pay = numbers[0]  
    b_pay1 = numbers[1]  
    b_limit = numbers[2]  
    b_pay2 = numbers[3]  
    monthly = numbers[4]  
    a_total = a_pay * monthly
    if monthly < b_limit:
        b_total = b_pay1
    else:
        b_total = b_pay1 + ((monthly - b_limit) * b_pay2)

    if a_total > b_total:
        print('#{} {}'.format(t, b_total))
    else:
        print('#{} {}'.format(t, a_total))