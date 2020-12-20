import sys; sys.stdin = open('input_data/4676.txt')

for t in range(1, int(input()) + 1):
    word = list(''.join(input()))
    numbers= int(input())
    where = list(map(int, input().split()))
    length = len(word) + 1
    check = [0]*length
    for i in where:
        check[i] += 1
    for i in range(length - 1, -1, -1):
        for _ in range(check[i]):
            word.insert(i, '-')
    print('#{} {}'.format(t, ''.join(word)))
