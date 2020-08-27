import sys
sys.stdin = open("input_data/1436.txt", 'r')

series = int(input())  # 몇번째 series인지 input
devil_number=[]        # 제목 하나씩 채워나갈거야
num_here = 666         # 1편부터
while len(devil_number) != series:  # series 수만큼 제목 채워나갈거다
    count = 0                       # 6이 3개인가 확인
    for char in str(num_here):      # int를 str로 변환해서
        if char == '6':
            count += 1
            if count == 3:          # 3개면 list에 넣고
                devil_number.append(num_here)
                break
        else: count = 0
    num_here += 1                    # 확인 숫자 +1 667, 668... 쭉
print(devil_number[-1])              # list 마지막꺼가 원하는 series

