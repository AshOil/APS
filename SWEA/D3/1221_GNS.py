import sys
sys.stdin = open('input_data/1221.txt',"r")

T = int(input())
for t in range(1,T+1):
    num_dict = {
        "ZRO" : 0, "ONE" : 0,
        "TWO": 0, "THR": 0,
        "FOR": 0, "FIV": 0,
        "SIX": 0, "SVN": 0,
        "EGT": 0, "NIN": 0,
    }
    tag, num = list(input().split())
    numbers = list(input().split())
    for number in numbers:
        num_dict[number] +=1

    print('#{}'.format(t))
    for key, value in num_dict.items():
        print('{} '.format(key)* value, end='')
    print()


