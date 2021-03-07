import sys; sys.stdin = open('input_data/13023.txt')

check = False
number, line = map(int, input().split())
ground = [[]*number for _ in range(number)]
for _ in range(line):
    i, j = map(int, input().split())
    ground[i].append(j)
    ground[j].append(i)


for _ in range(number):

