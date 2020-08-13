import sys
sys.stdin = open('input_data/2628.txt','r')
# 정보 주워담기
width, height = list(map(int,input().split()))
cutting = int(input())
cuttings = []
verti = [width]
hori = [height]
for _ in range(cutting):
    cuttings.append(list(map(int,input().split())))

#가로 / 세로 분류하기
for cut in cuttings:
    if cut[0] == 0:
        hori.append(cut[1])
    else:
        verti.append(cut[1])

# 분류한거 순서대로 분류하기
verti.sort()
hori.sort()
verti_len = len(verti)
hori_len = len(hori)

# 자른 선 크기별로 구분하기
verti_paper,hori_paper  = [0] * verti_len, [0] * hori_len
hori_paper[0], verti_paper[0] = hori[0], verti[0]
for i in range(1,verti_len):
    verti_paper[i] = verti[i]-verti[i-1]
for i in range(1, hori_len):
    hori_paper[i] = hori[i] - hori[i - 1]

# 크기 구하기
result = []
for i in hori_paper:
    for j in verti_paper:
        result.append(i*j)
print(max(result))



# 4,10 --> 4,6
# 2,3,8 --> 2 ,1 5