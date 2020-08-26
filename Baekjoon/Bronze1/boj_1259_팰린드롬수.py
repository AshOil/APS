import sys
sys.stdin = open('input_data/1259.txt',"r")
number = ''
while number != '0':
    number = input()
    if number == '0':
        pass
    else:
        if number == number[::-1]:
            print('yes')
        else:print('no')