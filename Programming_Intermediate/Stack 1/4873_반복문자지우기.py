import sys
sys.stdin= open("input_data/4873.txt",'r')

T = int(input())
for t in range(1, T+1):
    sentence = list(''.join(input()))
    print(sentence)
    check_result = True
    while check_result:
        length = len(sentence)
        for i in range(length-1):
            if sentence[i] == sentence[i+1]:
                sentence.pop(i)
                sentence.pop(i)
                break
        else:
            check_result = False
    print('#{} {}'.format(t, len(sentence)))





