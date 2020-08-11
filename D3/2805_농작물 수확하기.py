import sys
sys.stdin = open('input_data/2805.txt',"r")

T = int(input())
for t in range(1,T+1):
    length = int(input())
    num_lists = []
    result = 0
    start = length//2
    end = length//2 +1
    for i in range(length):
        num_lists.append(input())

    for idx, number in enumerate(num_lists):
        print(number[start:end])
        my_num = number[start:end]
        for i in my_num:
            result += int(i)
        if idx >= length//2:
            start += 1
            end -= 1

        else:
            start -= 1
            end += 1

    print('#{} {}'.format(t, result))
