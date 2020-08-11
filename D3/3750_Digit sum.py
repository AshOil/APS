import sys
sys.stdin = open('input_data/3750.txt',"r")

T = int(input())
for t in range(1,T+1):
    number = input()
    length = len(str(number))
    my_sum = number
    while length > 1:
        for num in my_sum:
            number += int(num)
        length = len(str(number))
    print(number)