
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

dx = [0, 0, 1, -1 , 1 ,1 ,-1 ,-1]
dy = [1, -1, 0, 0 , 1 , -1, 1 ,-1]

x = y= 1
for i in range(8):
    tx = x + dx[i]
    ty = y + dy[i]
    print(arr[tx][ty])

'''
6
4
8
2
9
7
3
1
'''