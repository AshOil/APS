import sys; sys.stdin = open('input_data/2748.txt')

N = int(input())
result = [0] * (N+1)

for i in range(1, N+1):
    if i <= 2:
        result[i] = 1
    else:
        result[i] = result[i-1] + result[i-2]
print(result[N])

