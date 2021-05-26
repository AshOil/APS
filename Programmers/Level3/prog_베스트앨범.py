genres = ["classic", "pop", "classic", "classic","jazz","pop", "Rock", "jazz"]
plays = [500, 600, 150, 800, 1100, 2500, 100, 1000]
music_list = {}
music_sum = {}
result = []

for i in range(len(plays)):
    if genres[i] not in music_list.keys():
        music_list[genres[i]] = [[plays[i], i]]
        music_sum[genres[i]] = plays[i]
    else:
        music_list[genres[i]].append([plays[i], i])
        music_sum[genres[i]] += plays[i]

for i in music_list:
    music_list[i] = sorted(music_list[i], key=(lambda x: (-x[0], x[1])))

sorted_sum = sorted(music_sum.items(), key=lambda x: x[1], reverse=True)
print(sorted_sum)

for genre in sorted_sum:
    result.append(music_list[genre[0]][0][1])
    if len(music_list[genre[0]]) >=2:
        result.append(music_list[genre[0]][1][1])
print(result)