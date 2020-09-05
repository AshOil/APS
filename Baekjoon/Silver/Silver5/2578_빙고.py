import sys
sys.stdin = open('input_data/2578.txt','r')

# 가로 더하기
num_list = []
for _ in range(5):
    num_list.append(list(map(int, input().split())))
bingo_list = num_list[:]
# 세로 더하기
for i in range(5):
    new_list = []
    for num in num_list:
        new_list.append(num[i])
    bingo_list.append(new_list)
    
# 대각선 1 더하기
new_list = []
for i in range(5):
    new_list.append(num_list[i][i])
    
# 대각선 2 더하기
new_list = []
for i in range(5):
    new_list.append(num_list[i][4-i])
bingo_list.append(new_list)

# 호출순서
call_list = []
for _ in range(5):
    call_list += list(map(int,input().split()))

# 하나씩 날리기
ending = False
for idx, num in enumerate(call_list, start=1):
    count = 0
    for bingo in bingo_list:
        if num in bingo:
            bingo.remove(num)
        if bingo == []:
            count +=1
        if count == 3:
            ending = True
            break
    if ending:
        print(idx)
        break


