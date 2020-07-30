import sys
sys.stdin = open('input_data/1926.txt',"r")

T = int(input())
numbers = list(range(1,T+1))
str_numbers = list(map(str, numbers))


# for number in str_numbers:
#     if '3' in number:
#         str_numbers[int(number)-1] = '-'
#     if '6' in number:
#         str_numbers[int(number)-1] = '-'
#     if '9' in number:
#         str_numbers[int(number)-1] = '-'
# print(str_numbers)

for number in str_numbers:
    count = 0
    for num in number:  
        
        if '3' in num:
            count += 1
        if '6' in num:
            count += 1
        if '9' in num:
            count += 1
        if count == 3:
            str_numbers[int(number)-1] = '---'
        elif count ==2:
            str_numbers[int(number)-1] = '--'
        elif count ==1:
            str_numbers[int(number)-1] = '-'
        else:
            pass

print(' '.join(str_numbers))



