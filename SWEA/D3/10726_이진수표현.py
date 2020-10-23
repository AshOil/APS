import sys; sys.stdin = open('input_data/10726.txt')

for t in range(1, int(input())+1):
    check, number = map(int, input().split())
    bi_num = []
    while number > 0:
        bi_num.append(number%2)
        number = number//2
    result = True
    if len(bi_num)>= check:
        for num in bi_num[0:check]:
            if not num:
                result = False
    else:
        result = False
    if result:
        print('#{} ON'.format(t))
    else:
        print('#{} OFF'.format(t))