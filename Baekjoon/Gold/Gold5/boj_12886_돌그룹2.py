import sys; sys.stdin=open('input_data/12886.txt')

def ANABADA(X, Y):
    Y -= X
    X += X
    if Y <= 0:
        return [-1, -1]
    return [X, Y]

stones = list(map(int, input().split()))
if stones[0] == stones[1] == stones[2]:
    print(1)
elif sum(stones)%3:
    print(0)
elif 0 in stones:
    print(0)
elif sum(stones)%2:
    print(0)
else:
    print(1)