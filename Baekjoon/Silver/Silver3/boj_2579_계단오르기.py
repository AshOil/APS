import sys; sys.stdin = open('input_data/2579.txt')

N = int(input())
stairs = [0] +[int(input()) for _ in range(N)]
# 3개로 나눠서 선택X, 전선택 X 이번선택 O, 전, 이번 둘다 선택 구분
check = [[0]*(N+1) for _ in range(3)]

check[1][1] = stairs[1]
for i in range(2, N+1):
    # 연속으로 밟는건, 저번에 밟은 것 + 이번 계단
    check[2][i] = check[1][i-1] + stairs[i]
    # 안밟는건, 연속밟은것과 전꺼 밟은 것 중에 큰값
    check[0][i] = max(check[1][i-1], check[2][i-1])
    # 이번에만 밟는건, 전에 안밟은것 + 이번 계단
    check[1][i] = check[0][i-1] + stairs[i]

# 이번 계단 포함 된 것 중, 큰 값
print(max(check[2][N], check[1][N]))