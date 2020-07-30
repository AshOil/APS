import sys
sys.stdin = open('input_data/1945.txt',"r")

T = int(input())
total = {}
for t in range(1, T+1):
    input_number = int(input())
    number_list = [2,3,5,7,11]
    for number in number_list:
        count = 0
        for _ in range(10):
            if input_number%number:
                total[number] = count
                break
            else:
                input_number = input_number/number
                count+= 1
    total_val = list(total.values())
    new_total = ' '.join(map(str,total_val))
                   

    print('#{} {}'.format(t, new_total))