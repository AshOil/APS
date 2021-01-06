import sys; sys.stdin = open('input_data/10804.txt')

mirror = {
    'p': 'q', 'q': 'p',
    'b': 'd', 'd': 'b'
}

for t in range(1, int(input()) + 1):
    print('#{}'.format(t), end=' ')
    word = list(' '.join(input()).split())
    while word:
        print(mirror[word.pop()], end='')
    print()

