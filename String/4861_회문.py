import sys
sys.stdin = open('input_data/4861.txt',"r")

T = int(input())
for t in range(1, T+1):
    size , length = list(map(int,input().split()))
    sentences = []
    for _ in range(size):
        sentences.append(input())
    for i in range(size):
        verti_word = ''
        for j in range(size):
            verti_word += sentences[j][i]

        sentences.append(verti_word)
    for sentence in sentences:
        for i in range(size-length+1):
            if sentence[i:i+length] == sentence[i:i+length][::-1]:
                print('#{} {}'.format(t,sentence[i:i+length] ))


### 1. 정보 불러오기(가로단어) ###
### 2. 세로 단어 만들어서 넣기 ###
### 3. 단어 리스트 돌아가면서 단어 비교하기 ###
# 1) 단어 길이 고려해서 한칸씩 옮기기
# 2) [::-1] 사용해서 뒤집기