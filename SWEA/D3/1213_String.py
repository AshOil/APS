import sys; sys.stdin = open('input_data/1213.txt', encoding='UTF8')

keep_going = True
while keep_going:
    try:
        t = int(input())
        my_word = input()
        string = input()
        result = 0
        for i in range(len(string) - len(my_word) + 1):
            if my_word == string[i:i+len(my_word)]:
                result += 1
        print('#{} {}'.format(t, result))
    except:
        keep_going = False