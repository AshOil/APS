import sys
sys.stdin = open('input_data/5188.txt')

def check(x, y):
    global result
    dx = [0, 1] #하, 우
    dy = [1, 0]


# ---------------------- 여기만 추가 -----------------------
    if result and sum(total) > min(result):
        return
# ---------------------- 여기만 추가 -----------------------
    #탈출조건
    if x== N-1 and y == N-1: # 맨밑에 도착/ 범위 잘 확인
        result.append(sum(total))
        return

    for i in range(2):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if new_x < N and new_y < N:
            total.append(tables[new_x][new_y])
            check(new_x, new_y)
            total.pop()


t = int(input())
for test_case in range(1, t+1):
    N = int(input())

    tables = []
    for _ in range(N):
        table = list(map(int, input().split()))
        tables.append(table)
    # print(tables)

    total = []
    result = []

    check(0,0)

    print('#{} {}'.format(test_case, min(result)+tables[0][0]))

