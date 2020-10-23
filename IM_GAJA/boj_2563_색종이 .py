import sys; sys.stdin = open('input_data/2563.txt')

paper_num = int(input())
ground = [[0]*100 for _ in range(100)]
result = 0
for _ in range(paper_num):
    x, y = map(int,input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if not ground[i][j]:
                ground[i][j] = 1
                result += 1
print(result)

