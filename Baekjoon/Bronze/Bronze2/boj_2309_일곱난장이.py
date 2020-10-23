import sys; sys.stdin = open('input_data/2309.txt')

from itertools import permutations

hobbit = [int(input()) for _ in range(9)]
print(hobbit)

hobbit_7 = list(permutations(hobbit,7))
for check in hobbit_7:
    if sum(check) == 100:
        for i in sorted(check):
            print(i)
        break