import sys
sys.stdin = open('input_data/1288.txt',"r")


T = int(input())


for t in range(1, T+1):
    number_list = ['1','2','3','4','5','6','7','8','9','0']
    number = int(input())
    for turn in range(1,10000):
        my_number = str(turn * number)
        for char in my_number:
            if char in number_list:
                number_list.remove(char)
                if not number_list:
                    print('#{} {}'.format(t,my_number))