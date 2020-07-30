import sys
sys.stdin = open("input_data/2027.txt","r")

for i in range(5):
    my_list = ['+','+','+','+']
    my_list.insert(i,'#')
    ''.join(my_list)
    for ii in my_list:
        print(ii, end='')
    print()   
