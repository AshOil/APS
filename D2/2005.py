### 질문해볼것!! 맞는데!!  ㅠㅠ ###


import sys
sys.stdin = open('input_data/2005.txt',"r")

T = int(input())

for t in range(1, T+1):
    print('# {}'.format(t))
    length = int(input())
    num_list = []
    for num in range(1,length+1):
        if num == 1:
            num_list.append(['1'])
        elif num ==2:
            num_list.append(['1','1']) 
        else:
            count_list = [ ]
            for _ in range(num):
                count_list.append('1')
            for in_num in range(1, num-1):               
                count_list[in_num] = str(int(num_list[num-2][in_num-1]) + int(num_list[num-2][in_num]))
            num_list.append(count_list)
    for in_list in num_list:
        print (' '.join(in_list))



        
    