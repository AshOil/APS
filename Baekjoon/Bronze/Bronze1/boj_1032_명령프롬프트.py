import sys
sys.stdin = open('input_data/1032.txt','r')

# 정보 input 받기
num = int(input())
numbers = []
for _ in range(num):
    numbers.append(input())
length = len(numbers[0])   # 글자 길이 // 모두 길이가 같아서 하나만 재면 된다.
result = ''

for i in range(length):
    my_check = numbers[0][i]
    for j in range(num):
        if numbers[j][i] != my_check:
            result += '?'
            break
    else:
        result += my_check
print(result)