import sys; sys.stdin = open('input_data/3376.txt')

def num_check(number):
    if triangle[number]:
        return triangle[number]
    else:
        small = num_check(number-3)
        big = num_check(number-2)
        triangle[number] = triangle[number-3] + triangle[number-2]


for t in range(1, int(input()) + 1):
    number = int(input())
    triangle = [0, 1, 1, 1] + [0]*(number-3)
    num_check(number)
    print('#{} {}'.format(t, triangle[-1]))