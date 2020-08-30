import sys
sys.stdin = open('input_data/4949.txt')



while True:
    try:
        sentence = input()
        if len(sentence)>1:
            stack = []
            for char in sentence:
                if char == '(' or char == '[' :
                    stack.append(char)
                elif char == ')':
                    if not stack:
                        print('no')
                        break
                    if stack.pop() != '(':
                        print('no')
                        break
                elif char == ']':
                    if not stack:
                        print('no')
                        break
                    if stack.pop() != '[':
                        print('no')
                        break
            else:
                if stack : print('no')
                else: print('yes')
    except EOFError:
        break
