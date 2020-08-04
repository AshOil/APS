## 시간문제 발생 ##

import math
import sys
sys.stdin = open('input_data/5688.txt',"r")

T = int(input())
for t in range(1,T+1):
    number = int(input())
    if abs(number**(1/3) - round(number**(1/3))) < 0.0001:
         print('#{} {}'.format(t, round(number**(1/3))))
    else:
        print('#{} -1'.format(t))


# T = int(input())
#
# for t in range(1,T+1):
#     number = int(input())
#     for i in range(1,number):
#         if i**3 > number:
#             print('#{} -1'.format(t))
#             break
#         elif number/(i**3) == 1:
#             print('#{} {}'.format(t, i))
#             break