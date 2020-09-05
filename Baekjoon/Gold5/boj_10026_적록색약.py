import sys
sys.stdin = open('input_data/10026.txt')
sys.setrecursionlimit(100000000)

# 방향 표시
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 함수 정의하기
def eye_test(x,y):
    visit[x][y] = 1   # 방문표시
    now = ground[x][y]  # 현재 보는 곳 색깔
    for i in range(4):  # 4방향 보면서
        tx = x + dx[i]
        ty = y + dy[i]
        # 같은색이고 안가봤으면
        if 0 <= tx < size and 0 <= ty < size and not visit[tx][ty] and ground[tx][ty] == now:
            eye_test(tx, ty)  # 가자!

# 정보 받아오기
size = int(input())
ground = [' '.join(input()).split() for _ in range(size)]
visit =[[0]*size for _ in range(size)] # 방문일지 만들기

count = 0 # 함수 몇번 돌아가나 확인

# 원래 상태부터 확인
for i in range(size):
    for j in range(size):
        if not visit[i][j]:
            eye_test(i, j)
            count += 1
print(count, end=' ')

# 지도 자체를 바꾸기
for i in range(size):
    for j in range(size):
        if ground[i][j] == 'G':
            ground[i][j] = 'R'

# 적록색약 상태로 확인
visit =[[0]*size for _ in range(size)]
count = 0

for i in range(size):
    for j in range(size):
        if not visit[i][j]:
            eye_test(i, j)
            count += 1
print(count)
