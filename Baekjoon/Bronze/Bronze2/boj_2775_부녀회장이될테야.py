import sys
sys.stdin = open('input_data/2775.txt', "r")

T = int(input())

for _ in range(T):
    floor = int(input())
    room = int(input())
    building = [[0]*room for _ in range(floor)]  # 0 층을 뺀 건물 만들기
    floor_0 = [i for i in range(1,room+1)]  # 0층 만들기
    building.insert(0,floor_0)  # 0층 추가하기

    for i in range(room):
        for j in range(1,floor+1):
            if i:
                building[j][i] = building[j][i-1] + building[j-1][i] # 옆집(왼쪽 )+ 아랫집
                # 옆집을 더하는 이유는 그 옆집은 아랫집 + 옆집 ... 계속하면 아랫집 전체의 합
                # 재귀같은 느낌
            else:
                building[j][i] = 1 # 1호에는 모두 1로 넣어주기
    print(building[j][i])
