import sys; sys.stdin=open('input_data/12886.txt')
from collections import deque

def ANABADA(X, Y):
    Y -= X
    X *= 2
    if Y <= 0:
        return [-1, -1]
    return [X, Y]

first = list(map(int, input().split()))
keep_going = True
first.sort()
check = dict()
char = ""
for num in first:
    char += str(num) + "|"
check[char] = 1
print(char)
print(check["asdf"])
already = [first]
Q = deque()
Q.append(first)
if keep_going:
    while Q:
        A, B, C = Q.popleft()
        if A == B == C:
            print(1)
            break
        if A != B:
            new = ANABADA(A, B) + [C]
            new.sort()
            if new[0] != -1 and not new in already:
                Q.append(new)
                already.append(new)
        if B != C:
            new = ANABADA(B, C) + [A]
            new.sort()
            if new[0] != -1 and not new in already:
                Q.append(new)
                already.append(new)
        if A != C:
            new = ANABADA(A, C) + [B]
            new.sort()
            if new[0] != -1 and not new in already:
                Q.append(new)
                already.append(new)
    else:
        print(0)
