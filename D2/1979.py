import sys
sys.stdin = open('input_data/1979.txt',"r")

T = int(input())

for t in range(1, T+1):
    map_size, word_length = list(map(int, input() .split()))
    map_list = []
    result = []
    for _ in range(map_size):
        map_list.append(list(map(int, input() .split())))

    
    # 가로 검색
    count = 0
    for hori in map_list:
        for blank in hori:
            if blank == 1:
                count +=1
            else:
                result.append(count)
                count = 0
        result.append(count)
        count = 0

    # 세로찾기
    count = 0
    for i in range(map_size):
        for verti in map_list:
            if verti[i] == 1:
                count += 1
            else:
                result.append(count)
                count = 0
        result.append(count)
        count = 0
    print('#{} {}'.format(t,result.count(word_length)))


            