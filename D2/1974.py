#### 진행중 (스도쿠 문제) ####


import sys

sys.stdin = open('input_data/1974.txt',"r")
num_dict = {}

for t in range(1,10):
    num_dict[t] = list(map(int, input() .split()))
result = True

# 가로부터 검사하자
for hori in num_dict.values():
    if sorted(hori) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        result = False

#세로 검사
for num in range(9):
    verti_check = []
    for verti in num_dict.values():
        verti_check.append(verti[num])
        verti_result = verti_check
    print(sorted(verti_check))
    if sorted(verti_check) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        result = False

#블록 검사
for num in range(9):
    block_check = []
    for verti in num_dict.values():
        verti_check.append(verti[num])
        verti_result = verti_check
    print(sorted(verti_check))
    if sorted(verti_check) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        result = False


print(result)




        
