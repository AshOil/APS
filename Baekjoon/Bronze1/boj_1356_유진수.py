import sys
sys.stdin = open("input_data/1356.txt",'r')

number = input()
length = len(number)
for cut in range(1,length):
    multi_a = multi_b = 1
    for i in range(cut):
        multi_a *= int(number[i])
    for j in range(cut,length):
        multi_b *= int(number[j])
    if multi_a == multi_b:
        print('YES')
        break
else:
    print('NO')