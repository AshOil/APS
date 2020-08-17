import sys
sys.stdin = open('input_data/2847.txt',"r")

length = int(input())
numbers = []
vacancy = [0]* length
for _ in range(length):
    numbers.append(int(input()))
max_val= 20000
idx = length-1
for num in numbers[::-1]:
    if num < max_val:
        vacancy[idx] = numbers[idx]
        max_val = num
        idx -= 1
    else:
        vacancy[idx] = vacancy[idx+1] -1
        idx -= 1
result = 0
for i in range(length):
    result += numbers[i] - vacancy[i]

print(result)


