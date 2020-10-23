import sys; sys.stdin = open('input_data/2605.txt')

students = int(input())
ticket = [0] + list(map(int,input().split()))
line_up = []
for i in range(1, students+1):
    line_up.insert(ticket[i], i)
print(*line_up[::-1])

