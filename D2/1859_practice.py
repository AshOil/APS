import sys
sys.stdin = open('input_data/1859.txt',"r")

T= int(input())

for t in range(1, T+1):
    days = int(input())
    price_data = list(map(int, input().split()))
    sell_price = [0] * days
    max_val = 0
    earn = 0
    for i in range(days-1, -1, -1):
        if price_data[i] > max_val:
            max_val = price_data[i]
            sell_price[i] = max_val
    for i in range(days):
        earn += (sell_price[i] - price_data[i])

    print('#{} {}'.format(t, earn))
