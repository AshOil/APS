import sys
sys.stdin = open('input_data/4864.txt',"r")

T = int(input())
for t in range(1, T+1):
    want = input()
    sentence = input()
    count = 0
    for i in range(len(sentence)-len(want) +1):
        if want == sentence[i: i+ len(want)]:
            count +=1
    print('#{} {}'.format(t,count))