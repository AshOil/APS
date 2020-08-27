import sys
sys.stdin= open("input_data/1362.txt",'r')

# 데이터 전체 불러오기

# 상태 확인할 함수 형성
def ConditionCheck(now):
    if still_alive:
        if standard/2 < now < standard*2:
            print("{} :-)".format(count))
        else:
            print("{} :-(".format(count))
    else:
        print("{} RIP".format(count))

count = 0                    # result 형식에 맞추기 위해 count
while True:
    try:
        input_data = list(input().split())       # 정보를 하나씩 불러오는데
        if input_data[0] == 0:                   # 앞자리가 0 이면 상황 종료
            break
        else:                                   # 0 이 아니면 시작
            if input_data[0].isalpha():         # 앞자리가 alphabet이면 수행
                if input_data[0] == 'F':        # F 면 살찌우고
                    now_weight += int(input_data[1])
                elif input_data[0] == "E":      # E 면 빼주는데
                    now_weight -= int(input_data[1])
                    if now_weight <= 0:          # 0보다 작으면 사망 ㅠ.ㅠ
                        still_alive = False   
            elif input_data[0] == '#':         # 앞자리가 # 이면 케이스 하나 종료
                count +=1                      # 숫자 올려주고
                ConditionCheck(now_weight)     # 상태 점검
            else:
                standard, now_weight = map(int, input_data)  # 앞자리가 alphabet도 아니고 #도 아니면 댕댕이 정보입력
                still_alive = True  # 현재 상태 살아있음
    except EOFError:
        break
