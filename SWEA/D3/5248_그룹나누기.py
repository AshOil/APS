import sys; sys.stdin = open('input_data/5248.txt')

def team_make(i):
    have_team[i] = 1
    if my_friend[i]:
        for j in my_friend[i]:
            if not have_team[j]:
                team_make(j)

for t in range(1, int(input()) + 1):
    student, line = map(int, input().split())
    line_data = list(map(int, input().split()))
    my_friend = [[] for _ in range(student + 1)]
    have_team = [0] * (student+1)
    for i in range(line):
        my_friend[line_data[i*2+1]].append(line_data[i*2])
        my_friend[line_data[i*2]].append(line_data[i*2+1])
    result = 0
    for i in range(1, student+1):
        if not have_team[i]:
            result += 1
            team_make(i)
    print('#{} {}'.format(t, result))

