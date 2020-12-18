import sys; sys.stdin = open('input_data/1234.txt')

for t in range(1, 11):
    length, number = input().split()
    number = list(map(int, ' '.join(str(number)).split()))
    check = True
    while check:
        for i in range(len(number) - 1):
            if number[i] == number[i + 1]:
                number.pop(i)
                number.pop(i)
                break
        else:
            check = False
    print('#{} {}'.format(t, ''.join(map(str, number))))
