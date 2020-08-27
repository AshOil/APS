import sys
sys.stdin = open('input_data/4839.txt',"r")

def binarysearch(list, key):
    start = 0
    end = len(list)-1
    count = 0
    while start<= end:
        count += 1
        middle = (start+end)//2
        if list[middle] == key:
            return count
        elif list[middle]>key:
            end = middle
        else: start = middle

T = int(input())

for t in range(1, T+1):
    total, for_a, for_b = list(map(int, input() .split()))
    total_list = list(range(1,total+1))
    a_count = binarysearch(total_list, for_a)
    b_count = binarysearch(total_list, for_b)
    if a_count > b_count:
        result = 'B'
    elif a_count == b_count:
        result = 0
    else:
        result = 'A'
    print('#{} {}'.format(t, result))