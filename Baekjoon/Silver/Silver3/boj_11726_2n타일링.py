import sys; sys.stdin = open('input_data/11726.txt')

N = int(input())
check = [0]*(N+1)

for i in range(1, N+1):
    if i < 3:
        check[i] = i
    else:
        check[i] = (check[i-1] + check[i-2])%10007
print(check[N])