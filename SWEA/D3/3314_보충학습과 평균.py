import sys; sys.stdin = open('input_data/3314.txt')

for t in range(1, int(input()) + 1):
    scores = list(map(int, input().split()))
    total = 0
    for score in scores:
        if score >=40:
            total += score
        else:
            total += 40
    print('#{} {}'.format(t, total//5))