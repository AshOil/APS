import sys
sys.stdin = open("input_data/4864.txt")

T = int(input())
for t in range(1, T+1):
    check = False
    want = input()
    sentence = input()
    for i in range(len(sentence)- len(want)):
        if want == sentence[i: i+len(want)]:
            check = True
            break
    if check:
        print('#{} 1'.format(t))
    else: print('#{} 0'.format(t))