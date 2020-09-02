import sys
sys.stdin = open("input_data/1224.txt", "r")

for t in range(1,11):
    N = int(input())
    testcase = input()
    stack = []
    number = []
    a = ''
    b=''
    c=''
    my =''
    result = []
    x=''
    y = ''
    dap = ''
    # 후위연산자 만들어주기
    for tc in testcase:
        if tc == '(':
            stack.append(tc)
        elif tc == '+' or tc == '-':
            if stack[-1] == '(':
                stack.append(tc)
            elif stack[-1] =='+' or stack[-1]=='-':
                c = stack.pop()
                number.append(c)
                stack.append(tc)
            elif stack[-1] =='/' or stack[-1]=='*':
                c= stack.pop()
                number.append(c)
                stack.append(tc)
            else:
                 stack.append(tc)
        elif tc == '*' or tc =='/':
            if stack[-1] == '(' or stack[-1] == '+' or stack[-1]=='-':
                stack.append(tc)
            elif stack[-1] == '*' or stack[-1]== '/':
                a = stack.pop()
                number.append(a)
                stack.append(tc)
        elif tc == ')':
            while stack[-1]!='(':
                if len(stack)!=0:
                    b = stack.pop()
                    number.append(b)

            if stack[-1] == '(':
                stack.pop()
        else:
            number.append(tc)
    print(number)

    # 계산
    for num in number:
        if num =='+':
            y = result.pop()
            x = result.pop()
            result.append(x+y)
        elif num == '-':
            y = result.pop()
            x = result.pop()
            result.append(x - y)
        elif num == '*':
            y = result.pop()
            x = result.pop()
            result.append(x * y)
        elif num == '/':
            y = result.pop()
            x = result.pop()
            result.append(x / y)
        else:
            result.append(int(num))

    print("#{} {}".format(t, *result))