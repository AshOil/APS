import sys
sys.stdin = open('input_data/1236.txt','r')

height, width = list(map(int,input().split()))
castle_map = []
for _ in range(height):
    castle_map.append(input())

garo_guard = []
sero_guard = []
for i in range(height):
    for j in range(width):
        if castle_map[i][j] =='X':
            sero_guard.append(i)
            garo_guard.append(j)
print(sero_guard)
print(garo_guard)

sero_vacancy = []
sero_vacancy = []
result = 0
for num in range(width):
    if num not in sero_guard:
        result += 1
        sero_guard.append(num)
        garo_guard.append(num)
for num in range(height):
    if num not in garo_guard:
        result += 1
        garo_guard.append(num)
print(result)
