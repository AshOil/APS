import sys
sys.stdin = open('input_data/9012.txt')

T = int(input())
for _ in range(T):
    PS = input()
    stack = []
    for string in PS:
        if string == '(':
            stack.append(string)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack: print('NO')
        else: print('YES')