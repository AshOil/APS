import sys
sys.stdin = open("input_data/2071.txt","r")

T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input() .split()))
    sum_numbers = sum(numbers)
    length = len(numbers)
    
    result = round((sum_numbers / length))
    
    print('#{} {}'.format(t, result))