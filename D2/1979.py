import sys
sys.stdin = open('input_data/1979.txt',"r")

T = int(input())

for t in range(1, T+1):
    map_size, word_length = list(map(int, input() .split()))
    map_list = []
    result = 0
    for _ in range(map_size):
        numbers = list(map(int, input() .split()))
        map_list.append(numbers)
    
    # 가로 검색
    count = 0
    for hori in map_list:
        start = 0
        end = word_length
        for _ in range(map_size-word_length):
            if not 0 in hori[start:word_length]:
                result += 1
            start += 1
            end += 1
        print(result)

            