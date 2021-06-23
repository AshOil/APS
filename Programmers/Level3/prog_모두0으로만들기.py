# 진행중
def solution(a, edges):
    size = len(a)
    Ground  = [[0]*size for _ in range(size)]
    if sum(a):
        return -1
    for edge in edges:
        Ground[edge[0]][edge[1]] = 1
        Ground[edge[1]][edge[0]] = 1
    result = 0
    for i in range(size):
        if a[i]:
            for j in range(size):
                if i != j and Ground[i][j] and abs(a[i]) > abs(a[i] + a[j]):
                    while a[i] and a[j]:
                        if a[i] < 0:
                            result += 1
                            a[i] += 1
                            a[j] -= 1
                        else:
                            result += 1
                            a[i] -= 1
                            a[j] += 1
    return result
