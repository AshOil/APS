import sys; sys.stdin = open('input_data/1011.txt')

for _ in range(int(input())):
    x, y = map(int, input().split())
    distance = y - x
    if distance == 1:
        print(1)
        continue
    peak = 0
    total = 0
    while total < distance//2:
        peak += 1
        total += peak
    now_gone = 2 * total - peak
    result = 2 * peak - 1
    distance -= now_gone
    while distance:
        result += distance // peak
        distance = distance % peak
        peak -= 1
    print(result)
