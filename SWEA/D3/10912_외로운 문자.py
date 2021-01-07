import sys; sys.stdin = open('input_data/10912.txt')

for t in range(1, int(input()) + 1):
    rest = []
    word = list(' '.join(input()).split())
    while word:
        char = word.pop(0)
        for i in range(len(word)):
            if char == word[i]:
                word.pop(i)
                break
        else:
            rest.append(char)
    if rest:
        rest.sort()
        print('#{} {}'.format(t, rest))
    else:
        print('#{} Good'.format(t))

