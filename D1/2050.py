import sys
sys.stdin = open("input_data/2050.txt","r")

T = input()

alpa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpa_dic = {}
start = 1
for char in alpa:
    alpa_dic[char] = start
    start += 1
result = ''

for i in T:
    print(alpa_dic[i], end =' ')