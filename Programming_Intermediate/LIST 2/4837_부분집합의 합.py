import sys
sys.stdin = open('input_data/4837.txt',"r")

T = int(input())

for t in range(1, T+1):
    length, target = list(map(int, input() .split()))
    numbers = list(range(1,13))

    mylist = []
    for i in range(1<<12):
        inlist = []
        for j in range(12):
            if i & (1<<j):
                inlist.append(numbers[j])
        mylist.append(inlist)
    result = 0
    for number in mylist:
        if len(number) ==length:

            my_sum = 0
            for num in number:
                my_sum += num

            if my_sum == target:
                result += 1

    print('#{} {}'.format(t, result))
