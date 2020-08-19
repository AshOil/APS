import sys
sys.stdin = open('input_data/1075.txt',"r")

number = input()
length = len(number)
divide = int(input())
my_num = int(number[0:length-2]) *100
for num in range(100):
    if (my_num + num)%divide:
        pass
    else:
        if num < 10:
            print('0'+str(num))
        else:
            print(num)
        break
