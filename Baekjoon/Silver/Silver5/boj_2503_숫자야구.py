import sys; sys.stdin = open('input_data/2503.txt')

N = int(input())
num_list = [list(map(int, input().split())) for _ in range(N)]
print(num_list)