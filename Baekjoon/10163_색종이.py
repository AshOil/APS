import sys
sys.stdin = open('input_data/10163.txt',"r")

paper_num = int(input())
paper_list = []
total_paper = [[0]*101 for _ in range(101)]
for _ in range(paper_num):
    paper_list.append(list(map(int, input().split())))
total_count =[]
for paper in paper_list[::-1]:
    count = 0
    for x in range(paper[0], paper[0] + paper[2]):
        for y in range(paper[1], paper[1] + paper[3]):
            if total_paper[x][y] == 0:
                total_paper[x][y] = 1
                count +=1
    total_count.append(count)
for _ in total_count[::-1]:
    print(_)