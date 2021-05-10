import sys; sys.stdin = open('input_data/13302.txt')

days, off_num = map(int, input().split())
off = list(map(int, input().split()))
check = [[0,0] for _ in range(days+1)]
check[1][0] = 10000
check[2][0] = 0000
print(check)

for i in range(3, days + 1):
    if i in off:continue



