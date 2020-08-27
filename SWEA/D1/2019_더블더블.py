import sys
sys.stdin = open("input_data/2019.txt","r")

T = int(input())

for i in range(T+1):
    print(2**i, end=' ')