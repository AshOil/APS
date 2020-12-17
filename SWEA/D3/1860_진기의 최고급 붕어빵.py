import sys; sys.stdin = open('input_data/1860.txt')

for t in range(1, int(input()) + 1):
    guest, cooltime, fish = map(int, input().split())
    guest_coming = list(map(int, input().split()))
    guest_coming.sort()
    if guest_coming[0] < cooltime:
        print('#{} Impossible'.format(t))
        continue
    cooked_fish = 0
    result = True
    for i in range(1, guest_coming[-1] + 1):
        if not i%cooltime:
            cooked_fish += fish
        while guest_coming and guest_coming[0] == i:
            now_guest = guest_coming.pop(0)
            if cooked_fish:
                cooked_fish -= 1
            else:
                result = False
        if result == False:
            print('#{} Impossible'.format(t))
            break
    else:
        print('#{} Possible'.format(t))




