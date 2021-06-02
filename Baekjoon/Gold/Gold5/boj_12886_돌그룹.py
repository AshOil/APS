import sys; sys.stdin=open('input_data/12886.txt')
from collections import deque

def ANABADA(X, Y):
    Y -= X
    X += X
    if Y <= 0:
        return [-1, -1]
    return [X, Y]

first = list(map(int, input().split()))
if sum(first)%3:
    print(0)
else:
    first.sort()
    already = [first]
    Q = deque()
    Q.append(first)
    while Q:
        A, B, C = Q.popleft()
        if A != B:
            new = ANABADA(A, B) + [C]
            if new[0] == new[1] == new[2]:
                print(1)
                break
            new.sort()
            if new[0] != -1 and new not in already :
                Q.append(new)
                already.append(new)
        if B != C:
            new = ANABADA(B, C) + [A]
            if new[0] == new[1] == new[2]:
                print(1)
                break
            new.sort()
            if new[0] != -1 and new not in already :
                Q.append(new)
                already.append(new)
        if A != C:
            new = ANABADA(A, C) + [B]
            if new[0] == new[1] == new[2]:
                print(1)
                break
            new.sort()
            if new[0] != -1 and new not in already :
                Q.append(new)
                already.append(new)
    else:
        print(0)
