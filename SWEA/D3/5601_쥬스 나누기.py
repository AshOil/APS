import sys; sys.stdin = open('input_data/5601.txt')

for t in range(1, int(input()) +1):
    person = int(input())
    print('#{}'.format(t), end=' ')
    for _ in range(person):
        print('1/{}'.format(person), end=' ')
    print()