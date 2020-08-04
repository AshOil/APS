import sys
sys.stdin = open('input_data/1208.txt',"r")

for t in range(1, 11):
    dumping_num = int(input())
    numbers = list(map(int, input() .split()))
    for _ in range(dumping_num+1):
        min_num = max_num = numbers[0]
        for number in numbers:
            if max_num < number :
                max_num = number
            if min_num > number :
                min_num = number
        numbers.remove(max_num)
        numbers.remove(min_num)
        numbers.append(max_num-1)
        numbers.append(min_num+1)

    print('#{} {}'.format(t, max_num - min_num))
