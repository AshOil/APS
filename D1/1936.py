import sys
sys.stdin = open("input_data/1936.txt","r")

numbers = list(map(int, input() .split()))
if numbers in [[3,2], [1,3], [2,1]]:
    print('A')
else:
    print('B')