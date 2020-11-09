import sys; sys.stdin = open('input_data/3980.txt')

def choose_player(i, total):
    global max_stat
    if i == 11:
        if max_stat < total:
            max_stat = total
        return
    for j in range(11):
        if visit[j] or not player_stat[i][j]: continue
        visit[j] = 1
        choose_player(i + 1, total + player_stat[i][j])
        visit[j] = 0
for t in range(int(input())):
    player_stat = [list(map(int, input().split())) for _ in range(11)]
    visit = [0] * 11
    max_stat = 0
    choose_player(0, 0)
    print(max_stat)
