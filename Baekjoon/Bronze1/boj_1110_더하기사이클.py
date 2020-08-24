import sys
sys.stdin = open('input_data/1110.txt','r')

number = original = input()
if len(original) <2:
    original = '0'+ original
result = 0
for i in range(100000):
    new_number = ''
    result += 1
    # 한자리수면 0 더해주기
    if int(number) < 10:
        end = number[-1]
        new = int(end)
    else:
        first = number[0]
        end = number[1]
        new = int(first) + int(end) # 둘을 더해서 새로 붙여줄 숫자

    # 붙여줄 수가 두자릿수면 뒤에것만 취한다.
    if new > 9:
        new = str(new)
        new = new[1]
    new_number = end+ str(new)
    number = new_number

    if original == new_number:
        print(result)
        break