# 예시는 맞는데 실제로 돌리면 9개만 답
import sys
sys.stdin = open('input_data/4874.txt')

T = int(input())
for t in range(1, T+1):
    try:
        cal = list(input().split())
        stack = []
        for char in cal:
            if char.isdigit():
                stack.append(int(char))
            elif char == '+':
                number = stack.pop() + stack.pop()
                stack.append(number)
            elif char == '-':
                first = stack.pop()
                second = stack.pop()
                number = second - first
                stack.append(number)
            elif char == '*':
                number = stack.pop() * stack.pop()
                stack.append(number)
            elif char == '/':
                first = stack.pop()
                second = stack.pop()
                number = second / first
                stack.append(int(number))
            else:
                result = stack.pop()
                if stack:
                    print('#{} error'.format(t))
                else:
                    print('#{} {}'.format(t, result))
    except IndexError:
        print('#{} error'.format(t))