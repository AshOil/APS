import sys
sys.stdin = open('input_data/7675.txt')

for t in range(1, int(input())+1):
    number = int(input())
    sentence = input().split()
    ending = ['.', '?', '!']
    print('#{}'.format(t), end=' ')
    result = 0
    for words in sentence:
        count = 0
        length = len(words)
        for char in words:
            if char.islower():
                count += 1
        if words[0].isupper() and count== length-1 :
            result +=1
        elif words[0].isupper() and words[-1] in ending and length-2 == count:
            result += 1
            print(result, end = ' ')
            result = 0
        elif words[-1] in ending:
            print(result, end = ' ')
            result = 0
    print()



