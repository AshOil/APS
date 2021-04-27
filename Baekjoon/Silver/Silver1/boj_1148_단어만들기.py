
import sys; sys.stdin = open('input_data/1148.txt')

check = True
word_list = []
word_count = [0] * 26
while check:
    word = input()
    if word == '-':
        check = False
    else:
        word_list.append(word)
check = True
while check:
    chars = input()
    for word in word_list:
        for char in word:
            pass

print(word_count)

