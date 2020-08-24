import sys
sys.stdin = open('input_data/1526.txt', "r")

number = input()
length = len(number)
result = ''

# 한자리 아랫수가 4 이하일 때 윗 자리수가 하나 빠지는 걸 못하겠음 ㅠㅠ
if length > 1:   # 한자리 수 일때 따로 처리
    keep_going = True
    if int(number[0:1]) < 44:    # 맨 앞자리가 4보다 작으면 그 이하 다 7777
        keep_going = False

    if keep_going:        # 맨 앞자리가 4가 아닐때
        count = length-1    # 뒤에서부터 탐색
        idx = 0
        while count >= 0:
            if int(number[count]) >=7 :
                result = '7' + result
            elif 7> int(number[count]) >=4 :
                result = '4' + result
            else:
                result = '7' +result
                number = str(int(number) - 10**(idx+1))    # 윗자리 숫자 하나 빼주기
            count -= 1
            idx += 1
        print(result)
    else:
        print('7' * (length - 1))
else:
    if int(number) >= 7:
        print('7')
    elif 7 > int(number) >= 4:
        print('4')




