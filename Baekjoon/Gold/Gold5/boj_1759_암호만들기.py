import sys; sys.stdin = open('input_data/1759.txt')

def make_password(i, word, essential, other):
    if len(word) == length:
        if essential == 0 or other < 2:
            return
        if word not in result:
            result.append(word)
            return
    if i == number:
        return
    now = chars[i]
    if chars[i] in essentical_list:
        make_password(i + 1, word+now, essential + 1, other)
        make_password(i + 1, word, essential, other)
    else:
        make_password(i + 1, word+now, essential, other + 1)
        make_password(i + 1, word, essential, other)

length, number = map(int, input().split())
essentical_list = ['a', 'e', 'i', 'o', 'u']
chars = list(input().split())
chars.sort()
result = []
make_password(0, '', 0, 0)
result.sort()
for i in result:
    print(i)

