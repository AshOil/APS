
import sys; sys.stdin = open('input_data/2251.txt')

bottle_list = list(map(int, input().split()))
numbers = len(bottle_list)
result = []
for bottle in bottle_list:
    if bottle <= bottle_list[-1]:
        result.append(bottle)
gap_list = []
for i in range(numbers):
    for j in range(i, numbers):
        gap = abs(bottle_list[i] - bottle_list[j])
        if gap not in gap_list and gap:
            gap_list.append(gap)
for gap in gap_list:
    if gap < bottle_list[-1]:
        result.append(gap)
result.sort()
print(*result)

