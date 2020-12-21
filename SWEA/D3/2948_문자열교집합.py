import sys;sys.stdin = open('input_data/2948.txt')

for t in range(1, int(input()) + 1):
    first, second = map(int, input().split())
    first_strings = list(input().split())
    second_strings = list(input().split())
    dict = {}
    result = 0
    for string in first_strings:
        dict[string] = 1
    for string in second_strings:
        if string in dict:
            result += 1
    print('#{} {}'.format(t, result))