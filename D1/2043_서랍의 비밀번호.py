import sys
sys.stdin = open("input_data/2043.txt","r")

numbers = list(map(int, input() .split()))
result = 1
for _ in range(numbers[1],numbers[0]):
    result += 1
print(result)