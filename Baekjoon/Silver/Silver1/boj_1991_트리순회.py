# 왜틀린지 몰겠쪙


import sys; sys.stdin = open('input_data/1991.txt')

def LookAround(char):
    for idx, branch in enumerate(Tree):
        if branch[0] == char:
            if char != '.':
                first.append(char)
                LookAround(Tree[idx][1])
                middle.append(char)
                LookAround(Tree[idx][2])
                last.append(char)
                break

Tree = [list(input().split()) for _ in range(int(input()))]
first = []
middle = []
last = []
LookAround('A')
print(' '.join(first))
print(' '.join(middle))
print(' '.join(last))