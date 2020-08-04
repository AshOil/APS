import sys
sys.stdin = open('input_data/4834.txt',"r")

T = int(input())

for t in range(1, T+1):
    length = int(input())
    numbers = input()
    numbers_count = {}
    for num in numbers:
        numbers_count[num] = numbers.count(num)
    max_count = max(numbers_count.values())
    max_list = []
    for i in numbers_count:
        if numbers_count[i] == max_count:
            max_list.append(int(i))
    print('#{} {} {}'.format(t, max(max_list), max_count))




