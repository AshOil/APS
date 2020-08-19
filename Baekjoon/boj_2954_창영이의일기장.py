import sys
sys.stdin = open('input_data/2954.txt',"r")

my_word = input()
new_word = ''
ban = ['a','e','i','o','u']
start = 0
while start < len(my_word):
    if my_word[start] in ban:
        new_word += my_word[start]
        start += 3
    else:
        new_word += my_word[start]
        start += 1
print(new_word)



