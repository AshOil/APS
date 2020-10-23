import sys; sys.stdin = open('input_data/2798.txt')
from itertools import permutations

### 재귀 ####
'''
def BBJP(x,calsum):
    if x == 3:
        result.append(calsum)
    else:
        BBJP(x+1, calsum + card_list[x])
        BBJP(x+1, calsum)

card_num , target = map(int,input().split())
card_list = list(map(int,input().split()))
result = []

BBJP(0,0)
print(result)
'''
card_num , target = map(int,input().split())
card_list = list(map(int,input().split()))
easy= list(permutations(card_list,3))
result = []
for in_easy in easy:
    if target - sum(in_easy) >=0:
        result.append(target - sum(in_easy))
print(target- min(result))

