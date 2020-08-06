import sys
sys.stdin = open('input_data/5356.txt',"r")

T = int(input())

for t in range(1,T+1):
    words = []
    for i in range(5):
        words.append(input())
    new_word = ''
    for num in range(15):
        for word in words:
            if len(word) > num:
                new_word += word[num]
    print('#{} {}'.format(t,new_word))


