import sys
sys.stdin = open('input_data/7576.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def Tomato(x,y):
    global count
    count += 1
    Q.append([x,y])
    while Q:
        t, y = Q.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx == height or tx < 0 or ty == width or ty <0 : continue
            if not visit[tx][ty] and ground[tx][ty] :continue
            Q.append([tx,ty])




## input 받아오기
width, height = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(height)]
# 탐방일지
visit = [[0]* width for _ in range(height)]
count = 0
Q= []
Tomato(5,3)
