import sys
sys.stdin = open('input_data/1216.txt',"r")

def Palindrome(sentenses):
    for i in range(100, 0, -1):
        for j in range(100 - i + 1):
            for sentence in sentences:
                if sentence[j:j + i] == sentence[j:j + i][::-1]:
                    return i
for _ in range(10):
    t = int(input())
    sentences = []
    for _ in range(100):
        sentences.append(input())
    for i in range(100):
        verti_word = ''
        for j in range(100):
            verti_word += sentences[j][i]
        sentences.append(verti_word)
    print('#{} {}'.format(t, Palindrome(sentences)))