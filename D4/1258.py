import sys
sys.stdin = open('input_data/1258.txt',"r")

T = int(input())

for t in range(1, T+1):
    # 지도 불러오기
    num_list =[]
    size = int(input())
    for _ in range(size):
        num_list.append(list(map(int, input().split())))
    quadrangle = 0
    result_list = []
# # 사각형 정보 뽑아내는 법
# 1. x랑 y좌표를 순회하는 이중 반복문을 만든다.
    for i in range(size):
        for j in range(size):
            count_x = count_y = 0
# 2. 돌고 있는 중에 0이 아닌 좌표를 만나면 그 위치에서 부터 가로 길이를 잰다. (가로 길이는 0을 만나는 위치까지)
            tx, ty = i , j
            if num_list[i][j] != 0:
                while num_list[i][ty] != 0 and ty+1 < size:
                    count_x += 1
                    ty += 1
# 3. 마찬가지로 세로 길이를 잰다. (세로 길이도 0을 만나는 위치까지)
                while num_list[tx][j] != 0 and tx+1 <size:
                    count_y += 1
                    tx += 1

# 4. 현재 위치, 가로 길이, 세로 길이 이용해서 숫자를 다 0으로 바꿔준다.
                for x in range (i,i+count_y):
                    for y in range(j,j+ count_x):
                        num_list[x][y] = 0


# 5. [가로 길이, 세로 길이, 가로*세로] 리스트 형태로 새로운 리스트에 저장해놓는다.
                result_list.append([count_y, count_x, count_x * count_y])

# 6. 사각형 개수를 하나 늘려준다.
                quadrangle += 1


#
# # 뽑아낸 사각형 정보 리스트 정렬하는 법
# 1. 선택 정렬을 쓴다.
# 2. 하지만 기본 선택 정렬이 단순히 값으로 정렬하는 거라면 이 문제에서는 가로*세로가 작은 순서대로 하고 가로*세로가 같다면 가로 길이가 작은 순서대로 정렬한다
# 3. 즉, 조건만 달라질 뿐 선택정렬이랑 원리가 똑같음
    for i in range(len(result_list)-1):
        min = i
        for j in range(i+1, len(result_list)):
            if result_list[i][2] > result_list[j][2]:
                min = j
                result_list[i], result_list[min] = result_list[min], result_list[i]
            if result_list[i][2] == result_list[j][2]:
                if result_list[i][0] > result_list[j][0]:
                    min = j
                    result_list[i], result_list[min] = result_list[min], result_list[i]



#
# # 출력
# 1. 정렬된 가로 세로 정보를 뽑아낸다.
    print('#{}'.format(t), end=' ')
    print('{}'.format(quadrangle), end=' ')
    for result in result_list:
        print(' '.join(map(str, result[0:2])), end=' ')
    print()