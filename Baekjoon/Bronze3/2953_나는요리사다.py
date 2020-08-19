import sys
sys.stdin = open('input_data/2953.txt',"r")

max_score = 0
winner = -1
for i in range(1,6):
    numbers = list(map(int, input(). split()))
    if sum(numbers) > max_score:
        max_score = sum(numbers)
        winner = i

print(winner, max_score)


