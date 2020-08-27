import sys
sys.stdin = open("input_data/4866.txt", 'r')

T = int(input())
for t in range(1, T+1):
    check_condition = True
    check_please = input()
    stack = []
    for char in check_please:
        # 여는 괄호는 바로 채우고
        if char == '(' or char == '{':
            stack.append(char)

        # 닫는 괄호는 분류
        elif char == ')':
            if stack:
                if stack.pop(-1) != '(':
                    check_condition = False
                    break
            else:
                check_condition = False
                break
        elif char == '}':
            if stack:
                if stack.pop(-1) != '{':
                    check_condition = False
                    break
            else:
                check_condition = False
                break
    if stack:
        check_condition = False

    if check_condition: print('#{} 1'.format(t))
    else: print('#{} 0'.format(t))

