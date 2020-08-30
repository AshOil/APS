'''
다음주 시험 출제 가능성 문제

[백준에서 관련 문제 풀어볼것]
DSF 출제 가능성 높다! (2차 배열 형태로 입력)
2차배열 형태로 입력을 주고 그걸 처리
'''

arr = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0]
]

'''
이런 섬이 있다고 생각할 때, 각각의 1이 하나의 정점으로 생각.
상하좌우 탐색후 섬 전체 파악할 수 있나 확인
'''

N = len(arr)
dx = [ 0, 0, 1, -1]
dy = [ 1, -1, 0, 0]

visit = [[0] * N for _ in range(N)]

def DSF(x, y):  # 각 항을 정점처럼 생각해야하기 때문에 x,y 받아옴
    visit[x][y] = 1
    for i in range(4):
        tx, ty = x +dx[i], y + dy[i]  # 임시 좌표 만들기
        if tx < 0 or tx == N or ty <0 or ty == N : continue  # 경계 벗어난 곳 거르기
        if arr[tx][ty] == 0 or visit[tx][ty] ==1 : continue  # 방문한곳 거르기  #땅이 아닌곳 거르기
        DSF(tx, ty)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            DSF(i, j)

for lst in arr:
    print(*lst)
print('---')
for lst in visit:
    print(*lst)