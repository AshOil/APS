import sys; sys.stdin = open('input_data/2477.txt')

melons = int(input())
data = [list(map(int,input().split())) for _ in range(6)]
data.append(data[0])
data.append(data[1])
# 1부터 돌리는데
for i in range(1, 7):
    if data[i-1][0] == data[i+1][0]: # 앞과 뒤의 방향이 같을 때
        if data[i][0]>2: # 세로방향
            small_width = data[i][1]
        else: # 가로방향
            small_height = data[i][1]
width_list = []
height_list = []
# 가장 큰 사각형 구하기
for in_data in data:
    if in_data[0]>2:
        width_list.append(in_data[1])
    else:
        height_list.append(in_data[1])
big = max(width_list) * max(height_list)
small = small_width * small_height
print((big-small)*melons)