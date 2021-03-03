import sys;
sys.stdin = open('input_data/1942.txt')

for _ in range(3):
    start, end = input().split()
    start_list = list(map(int, start.split(":")))
    end_list = list(map(int, end.split(":")))
    print(start_list)
    print(end_list)
