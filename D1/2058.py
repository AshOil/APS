import sys
sys.stdin = open("input_data/2058.txt","r")

T = input()

numbers = []
for i in T:
    numbers.append(int(i))
result = sum(numbers)
print(result)