import sys
sys.stdin = open("input_data/1938.txt","r")

numbers = list(map(int, input() .split()))
a = numbers[0]
b = numbers[1]
print(a + b)
print(a - b)
print(a * b)
print(int(a/b))