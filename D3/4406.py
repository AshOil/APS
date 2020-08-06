import sys
sys.stdin = open('input_data/4406.txt',"r")

T = int(input())
cant_see = 'aeiou'
for t in range(1, T+1):
    word = input()
    new_word = ''
    for char in word:
        if not char in cant_see:
            new_word += char
    print('#{} {}'.format(t, new_word))
