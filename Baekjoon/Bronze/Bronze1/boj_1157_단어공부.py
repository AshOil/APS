## 이게 왜 틀려


import sys
sys.stdin = open('input_data/1157.txt',"r")

words = input().upper()
result = ''
max_num = 0
for word in words:
    num = words.count(word)
    if num > max_num:
        max_num = num
        result = word
    elif num == max_num:
        if result != word:
            print('?')
            break
else: print(result[0])

