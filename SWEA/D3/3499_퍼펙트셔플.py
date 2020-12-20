import sys; sys.stdin =open('input_data/3499.txt')

for t in range(1, int(input()) + 1):
    length = int(input())
    cards = list(input().split())
    shuffle = []
    if length%2:
        A_cards = cards[:length // 2 + 1]
        B_cards = cards[length // 2 + 1:]

    else:
        A_cards = cards[:length//2]
        B_cards = cards[length//2:]
    while A_cards or B_cards:
        if A_cards:
            shuffle.append(A_cards.pop(0))
        if B_cards:
            shuffle.append(B_cards.pop(0))
    print('#{} {}'.format(t, ' '.join(shuffle)))