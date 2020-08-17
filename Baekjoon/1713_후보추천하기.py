import sys
sys.stdin = open('input_data/1713.txt','r')

nominate = int(input())
votes = int(input())
vote_list = list(map(int, input().split()))
final_nominate = list([0]* 3 for _ in range(nominate))

min_vote = 1000
for idx, vote in enumerate(vote_list):
    print(idx)
    for vacancy in final_nominate:
        if vacancy[1] < min_vote:
            min_vote = vacancy[1]
        if vacancy[0] == 0:
            vacancy[0] = vote
            vacancy[1] = 1
            vacancy[2] = idx
            break
        else:
            pass

print(final_nominate)
