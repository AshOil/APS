import sys
sys.stdin= open("input_data/1592.txt",'r')

# data 받아오기
friends, max_catch, give = list(map(int, input().split()))
catch = [0] * friends
catch[0] = 1
result = 0

# 공 주기
ball_here = 0   # 현재 공 위치
while max(catch) < max_catch:
    result += 1
    if catch[ball_here]%2:   # 던질 방향 구하기
        ball_here += give
    else:
        ball_here -= give

    if ball_here >= friends:  # 원형 구현하기
        ball_here -= friends
    elif ball_here < 0:
        ball_here += friends
    catch[ball_here] +=1

print(result)