## 진행중 ##

import sys
sys.stdin = open('input_data/5431.txt',"r")

T = int(input())

for t in range(1,T+1):
    words = []
    for i in range(5):
    words.append(i)
    new_word = []
    for word in words:
        new_word += word[0]