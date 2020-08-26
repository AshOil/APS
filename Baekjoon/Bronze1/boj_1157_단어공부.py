## 이게 왜 틀려


import sys
sys.stdin = open('input_data/1157.txt',"r")

words = input().upper()
count_dict = {}
for word in words:
    num = words.count(word)
    count_dict[word] = num
result = []
max_num = max(count_dict.values())
for key, value in count_dict.items():
    if value == max_num:
        result.append(key)
if len(result) > 1: print('?')
else: print(result[0])

