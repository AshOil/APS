import sys
sys.stdin = open('input_data/1076.txt',"r")

colors = ['black', 'brown', 'red', 'orange','yellow','green', 'blue', 'violet', 'grey', 'white']
my_color = []
for _ in range(3):
    my_color.append(input())
my_num = 0
for idx1, col in enumerate(my_color):
    for idx2, color in enumerate(colors):
        if col == color:
            if idx1 == 0:
                my_num += idx2 * 10
            elif idx1 == 1:
                my_num += idx2
            else:
                my_num *= 10**idx2

print(my_num)