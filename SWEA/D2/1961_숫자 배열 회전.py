import sys
sys.stdin = open('input_data/1961.txt',"r")

T = int(input())
for t in range(1, T+1):
    size = int(input())
    number_list = []
    for _ in range(size):
        number_list.append(list(map(int,input().split())))
