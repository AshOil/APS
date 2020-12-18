import sys; sys.stdin = open('input_data/1230.txt')

def I_method():
    spot = int(orders.pop(0))
    numbers = int(orders.pop(0))
    for _ in range(numbers):
        password.insert(spot, orders.pop(0))
        spot += 1

def D_method():
    spot = int(orders.pop(0))
    numbers = int(orders.pop(0))
    for _ in range(numbers):
        password.pop(spot)

def A_method():
    numbers = int(orders.pop(0))
    for _ in range(numbers):
        password.append(orders.pop(0))

for t in range(1, 11):
    length = int(input())
    password = list(input().split())
    order_length = int(input())
    orders = list(input().split())
    while orders:
        action = orders.pop(0)
        if action == 'I':
            I_method()
        elif action == 'D':
            D_method()
        else:
            A_method()
    print('#{} {}'.format(t, ' '.join(password[:10])))