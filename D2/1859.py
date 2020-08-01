## 진행중 ###

import sys
sys.stdin = open('input_data/1859.txt',"r")


T = int(input())


for t in range(1, T+1):
    length = int(input())
    numbers = list(map(int, input() .split()))
    result = 0
    total = 0
    JJAM = sorted(numbers).reverse
    print(JJAM)
    

