import sys
sys.stdin = open("input_data/1224.txt", "r")

#정보 불러오기
for t in range(1,11):
    length = int(input())
    calcul = input()
    num_stack = []   # 숫자 넣어줄 곳
    gaesan_stack = []  # 계산식 넣어줄  고

    # input한거 전체 돌리는데
    for cal in calcul:
        # 숫자면 바로 넣어주기
        if cal.isdigit():
            num_stack.append(cal)
        # 열린 괄호도 바로 넣고
        elif cal =='(':
            gaesan_stack.append(cal)
        # 닫는 괄호나오면 열린괄호까지 먹은거 다 뱉어
        elif cal ==')':
            while gaesan_stack[-1] != '(':
                num_stack.append(gaesan_stack.pop())
            gaesan_stack.pop()
        # 곱하기(나누기) 나오면
        elif cal =='*':
            # top에 있던게 또 곱하기면 바로 숫자쪽에 넣어주기
            # top을 빼서 숫자쪽에 넣고, 새로 나온 것을 계산쪽에 넣는거지만 나누기가 없으므로 썜썜
            if gaesan_stack[-1] == '*':
                num_stack.append(cal)
            # 나머지는 그냥 넣어줘
            else:
                gaesan_stack.append(cal)
        # 더하기(빼기) 나오면
        elif cal =='+':
            # top에 있던게 또 더하기면 바로 숫자쪽에 넣어주기
            # top을 빼서 숫자쪽에 넣고, 새로 나온 것을 계산쪽에 넣는거지만 빼기가 없으므로 썜썜
            if gaesan_stack[-1] =='+':
                num_stack.append(cal)
            #만일 top이 곱하기 나오면 곱하기 빼서 넣고, 더하기 계산에 넣기
            elif gaesan_stack[-1] == '*':
                num_stack.append(gaesan_stack.pop())
                gaesan_stack.append(cal)
            # 나머지가 있으면 그대로 넣기
            else:
                gaesan_stack.append(cal)

    result = []  # 계산공간
    # 계산
    for num in num_stack:
        if num =='+':
            y = result.pop()
            x = result.pop()
            result.append(x+y)
        elif num == '*':
            y = result.pop()
            x = result.pop()
            result.append(x * y)
        else:
            result.append(int(num))

    print("#{} {}".format(t, *result))

