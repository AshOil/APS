# 다중트리 써야돼!! ㅠㅠㅠㅠㅠ 패스 ㅠㅠㅠ

import sys; sys.stdin = open('input_data/1068.txt')

def CountCheck(num):
    global count
    if num == target: return
    left = tree[num][0]
    right = tree[num][1]
    if right:
        CountCheck(right)
    if left:
        CountCheck(left)
    else:
        count.append(1)


dot = int(input())
numbers = list(map(int, input().split()))
target = int(input())
tree = [[] for _ in range(dot+1)]
for idx, num in enumerate(numbers):
    tree[num].append(idx)
print(tree)


