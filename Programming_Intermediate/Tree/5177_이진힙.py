import sys; sys.stdin = open('input_data/5177.txt')

def Push(x):
    global hsize
    hsize += 1
    Heap[hsize] = x
    child, parent  = hsize, hsize//2
    while parent:
        if Heap[parent] > Heap[child]:
            Heap[parent], Heap[child] = Heap[child], Heap[parent]
            child = parent
            parent = child//2
        else:
            break

for t in range(1, int(input())+1):
    length = int(input())
    numbers = list(map(int, input().split()))

    hsize = 0
    Heap = [0]* (length +1)

    for num in numbers:
        Push(num)

    result = 0
    while hsize:
        hsize = hsize//2
        result += Heap[hsize]
    print('#{} {}'.format(t, result))
