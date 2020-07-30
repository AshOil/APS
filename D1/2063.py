import sys
sys.stdin = open("input_data/2063.txt","r")

T = int(input())

numbers = list(map(int, input() .split()))
new_numbers = sorted(numbers)
length = len(new_numbers)

result = new_numbers[length//2]

print(result)