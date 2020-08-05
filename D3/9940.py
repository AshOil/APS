import sys
sys.stdin = open('input_data/9940.txt',"r")

T = int(input())

for t in range(1, T+1):
    result = True
    length = int(input())
    numbers = list(map(int, input().split()))
    for num in range(1, length+1):
        if not num in numbers:
            result = False

    if result: print('#{} Yes'.format(t))
    else : print('#{} No'.format(t))
