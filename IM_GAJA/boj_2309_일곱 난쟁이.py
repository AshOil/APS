import sys; sys.stdin = open('input_data/2309.txt')
from itertools import combinations
hobbit = [int(input()) for _ in range(9)]
seven_hobbit = list(combinations(hobbit, 7))
for seven in seven_hobbit:
    if sum(seven) == 100:
        results = seven
        break
for result in sorted(results):
    print(result)