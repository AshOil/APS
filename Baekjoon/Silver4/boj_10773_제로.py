import sys
sys.stdin = open('input_data/10773.txt')

numbers = int(input())

stack = []
for _ in range(numbers):
    num = int(input())
    if num: stack.append(num)
    else: stack.pop()

print(sum(stack))