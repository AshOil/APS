n = 2
words = ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']

from collections import deque
def solution(n, words):
    already = deque()
    words = deque(words)
    before_word = ''
    for i in range(0, len(words)):
        word = words.popleft()
        if before_word:
            if before_word[-1] != word[0] or word in already:
                return [i % n + 1, i//n + 1]
            else:
                already.append(word)
                before_word = word
        else:
            before_word = word
            already.append(word)
    else:
        return [0, 0]

print(solution(n, words))