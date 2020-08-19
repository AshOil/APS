import sys
sys.stdin = open('input_data/1159.txt',"r")

player_num = int(input())
players = []
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha_dict= {}
for char in alpha:
    alpha_dict[char] =0
for _ in range(player_num):
    players.append(input())
for player in players:
    alpha_dict[player[0]] += 1
result =''
for key, value in alpha_dict.items():
    if value >= 5:
        result += key

if result: print(result)
else: print('PREDAJA')