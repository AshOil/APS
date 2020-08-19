import sys
sys.stdin = open('input_data/8979.txt',"r")

country, my_country = list(map(int, input().split()))
whole_score = []
for _ in range(country):
    score = list(map(int, input().split()))
    whole_score.append(score)
    if score[0] == my_country:
        my_gold, my_silver, my_bronze = score[1:4]
result = 1
for score in whole_score:
    if score[1] > my_gold:
        result += 1
    elif score[1] == my_gold:
        if score[2] > my_silver:
            result += 1
        elif score[2] == my_silver:
            if score[3] > my_bronze:
                result += 1
print(result)


