## 실패~~ ##

import sys
sys.stdin = open('input_data/4881.txt')


def MinFind(row, score):
    global min_sum
    # row : 여태까지 뽑아낸 개수
    # 개수가 size랑 같으면 그동안 더한값 비교
    stack = []
    stack.append([row, score])
    while stack:
        row, score = stack.pop()
        if row == size:
            if score < min_sum:
                min_sum = score
            return min_sum
        for i in range(size):  # 하나씩 돌면서
            if not check[i]:  # 뽑은적 없는 idx면
                check[i] = 1  # 확인도장 찍고
                stack.append([row + 1, score + arr[row][i]])
                check[i] = 0
                # check[i] = 0  # 원래 상태 돌려주기
    return min_sum


T = int(input())
for t in range(1,T+1):
    min_sum = 10000
    size = int(input())
    arr = [list(map(int,sys.stdin.readline().split())) for _ in range(size)]
    # 방문일지
    check = [0] * size
    print('#{} {}'.format(t,MinFind(0,0)))
