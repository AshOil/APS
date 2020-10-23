import sys; sys.stdin = open('input_data/2559.txt')

length = int(input())
numbers = list(map(int,input().split()))
up_check = [1]*length
down_check = [1]*length

for i in range(1, length):
    if numbers[i]>=numbers[i-1]:
        up_check[i] += up_check[i-1]
    if numbers[i]<=numbers[i-1]:
        down_check[i] += down_check[i-1]
print(max(up_check+down_check))