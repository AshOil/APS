import sys; sys.stdin = open('input_data/1865.txt')

def doWork(result, havetodo, count):
    global max_num
    count += 1
    if result == 0:
        return
    if count == worker+1:
        if result > max_num:
            max_num = result
    for i in range(worker):
        if already_done[i]:
            already_done[i] = 0
            for j in range(worker):
                if havetodo[j]:
                    havetodo[j] = 0
                    doWork(result * worksheet[i][j], havetodo, count)
                    havetodo[j] = 1
                    break
            already_done[i] = 1



for t in range(1, int(input()) + 1):
    worker = int(input())
    worksheet = [list(map(int, input().split())) for _ in range(worker)]
    havetodo = [1] * worker
    already_done = [1] * worker
    max_num = 0
    doWork(1, havetodo, 0)
    print(max_num)