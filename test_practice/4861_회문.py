import sys
sys.stdin = open("input_data/4861.txt")

T = int(input())
for t in range(1,T+1):
    size, length = map(int,input().split())
    sentences = [input() for _ in range(size)]
    for i in range(size):
        sero = ''
        for sentence in sentences:
            sero += sentence[i]
        sentences.append(sero)

    for sentence in sentences:
        for i in range(size-length+1):
            if sentence[i : i+length] == sentence[i : i+length][::-1]:
                print('#{} {}'.format(t, sentence[i : i+ length]))


