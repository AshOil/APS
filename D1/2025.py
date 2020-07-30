import sys
sys.stdin = open("input_data/2025.txt","r")

number = int(input())
count = 0
for i in range(number +1):
    count += i
print(count)