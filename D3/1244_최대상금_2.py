import sys
sys.stdin = open('input_data/1244.txt',"r")

T = int(input())
for t in range(1,T+1):
    number, turn = list(map(int, input().split()))
    num_list = list(map(int,[num for num in str(number)]))
    length = len(num_list)
    if turn >5:
        print('순서대로!')

