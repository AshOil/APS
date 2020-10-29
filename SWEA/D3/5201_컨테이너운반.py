import sys; sys.stdin = open('input_data/5201.txt')

for t in range(1, int(input()) + 1):
    container_num, Fedex_num = map(int, input().split())
    baggage = sorted(list(map(int, input().split())))
    Fedex = sorted(list(map(int, input().split())))
    result = 0
    for i in Fedex:
        carry = 0
        for j in baggage:
            if i >= j:
                 carry = j
        if carry:
            baggage.remove(carry)
        result += carry
    print('#{} {}'.format(t, result))
