import sys
sys.stdin = open('input_data/2495.txt',"r")

T= int(input())
for _ in range(T):
    # 어짜피 한글자씩 돌릴거라 str형태로 받음
    numbers = input()
    length = len(numbers)
    # indexError 방지하기 위해 앞에 0 하나 넣어주기
    numbers = '0'+ numbers
    print(numbers)
    result = 0
    count = 1
    # 본인이랑 한칸 뒤 비교하기
    for i in range(length):
        if numbers[i] == numbers[i+1]:
            count += 1
        else: count = 1
        # 가장 큰값만 뽑아내려고
        if count > result:
            result = count
    print(result)





