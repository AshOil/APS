import sys
sys.stdin = open('input_data/2615.txt','r')

numbers=[]
for _ in range(19):
    numbers.append(list(map(int,input().split())))

dx = [0,0,-1,1,1,-1,1,-1]
dy = [-1,1,0,0,1,-1,-1,1]

count = 0
my_num = 0
i = 0
for x in range(19):
    for y in range(19):
        count = 0
        if numbers[x][y]:
            my_num = numbers[x][y]
        for i in range(8):
            tX = x + dx[i]
            tY = y + dy[i]
            if 19> tX >= 0 and 19 >tY >= 0
                print(arr[testX][testY], end = ' ')
        if numbers[i][j] != 0:
            who = numbers[i][j]



        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if testX >= 0 and testX < N and testY >= 0 and testY < M:
                print(arr[testX][testY], end = ' ')