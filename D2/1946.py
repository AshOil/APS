import sys
sys.stdin = open('input_data/1946.txt',"r")


T = int(input())

for t in range(1, T+1):
    print('#{}'.format(t))
    ingredients = int(input())
    line_count = 0
    for ingredient in range(ingredients):
        input_info= list((input() .split()))
        char, number = input_info
        for num in range(int(number)) :
            if line_count < 9:
                line_count += 1
                print(char,end='')
            else:
                print(char,end='')
                print('')
                line_count  = 0
    print('')


    











    