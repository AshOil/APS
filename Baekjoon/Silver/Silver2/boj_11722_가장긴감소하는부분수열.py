import sys; sys.stdin = open('input_data/11722.txt')

n = int(input())
nums = list(map(int, input().split()))
check = [1] * n

for i in range(1, n):
    for j in range(i):
        if nums[j] > nums[i]:
            check[i] = max(check[i], check[j]+1)
print(max(check))
