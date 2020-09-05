import sys
sys.stdin = open('input_data/10828.txt')

number = int(input())
stack = []
for _ in range(number):
    data = sys.stdin.readline().split()
    print(data)
    # push일때
    if len(data)> 1:
        stack.append(data[1])
    # pop일때
    elif data[0] == 'pop':
        if stack: print(stack.pop(-1))
        else: print('-1')
    # size일떄
    elif data[0] == 'size':
        print(len(stack))
    # empty일때
    elif data[0] == 'empty':
        if stack: print('0')
        else: print('1')
    # top일때
    else:
        if stack: print(stack[-1])
        else: print('-1')