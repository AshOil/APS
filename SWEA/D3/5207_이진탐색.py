import sys; sys.stdin = open('input_data/5207.txt')

def halfCut(lo, hi):
    global my_way
    global count
    mid = (lo + hi)//2
    if number == my_list[mid]:
        count += 1
        return
    elif number < my_list[mid]:
        if my_way == 'left':
            return
        else:
            my_way = 'left'
            halfCut(lo, mid - 1)
    elif my_list[mid] < number:
        if my_way == 'right':
            return
        else:
            my_way = 'right'
            halfCut(mid + 1, hi)

for t in range(1, int(input()) + 1):
    length, num_kind = map(int, input().split())
    my_list = list(map(int, input().split()))
    my_list.sort()
    numbers = list(map(int, input().split()))
    count = 0
    for number in numbers:
        if number in my_list:
            my_way = ''
            halfCut(0, length-1)
    print('#{} {}'.format(t, count))
