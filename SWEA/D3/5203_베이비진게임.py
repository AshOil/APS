import sys; sys.stdin = open('input_data/5203.txt')

def cardCheck(player):
    for i in range(10):
        if player.count(i) == 3:
            return True
        if i in player and i+1 in player and i+2 in player:
            return True



for t in range(1, int(input()) + 1):
    cards = list(map(int, input().split()))
    player1 = []
    player2 = []
    for i, card in enumerate(cards):
        if i % 2:
            player2.append(card)
            cardCheck(player2)
            if cardCheck(player2):
                print('#{} 2'.format(t))
                break
        else:
            player1.append(card)
            cardCheck(player1)
            if cardCheck(player1):
                print('#{} 1'.format(t))
                break
    else:
        print('#{} 0'.format(t))