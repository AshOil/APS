import sys; sys.stdin = open('input_data/10158.txt')

height, width = map(int, input().split())
x, y = map(int, input().split())
time = int(input())

x += time
y += time
if (x//height)%2:
    result_x = height-x%height
else:
    result_x = x%height
if (y//width)%2:
    result_y = width-y%width
else:
    result_y = y%width
print(result_x,result_y)


# x_way = 1
# y_way = 1
# for i in range(time):
#     x += x_way
#     y += y_way
#     if x == height:
#         x_way = -1
#     if y == width:
#         y_way = -1
#     if x == 0:
#         x_way = -1
#     if y == 0:
#         y_way = 1
# print(x,y)



