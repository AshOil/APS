import sys
sys.stdin= open("input_data/1210.txt", 'r')

# 정보 불러오기
for _ in range(10):
    test_num = int(input())
    labbers = []
    for _ in range(100):
        labbers.append(list(map(int, input().split())))
    # 출발점 찾기
    for i in range(100):
        start = i
        j = 0
        # 출발점 찾았을 때
        if labbers[j][i] == 1 :
            # 바닥 도착할 때 까지
            while j < 100:
                # 오른쪽에 사다리 있으면 쭉 이동
                if i+1 < 100 and labbers[j][i+1] == 1 :
                    while i+1 < 100 and labbers[j][i+1] == 1:
                        i += 1
                # 왼쪽에 사다리 있으면 쭉 이동
                elif i-1 > -1 and labbers[j][i-1] == 1 :
                    while i-1 > -1 and labbers[j][i-1] == 1:
                        i -= 1
                # 좌우 사다리 이동 끝났으면 한칸 내려가기
                j += 1
            # 바닥 도착 했을 때
            if labbers[j-1][i] == 2:
                print('#{} {}'.format(test_num,start))
                break


