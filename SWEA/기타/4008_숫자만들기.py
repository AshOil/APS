import sys; sys.stdin = open('input_data/4008.txt')

def treeCalculate(num, plus, minos, multi, div, count):
    count += 1
    if count == length:
        result_list.append(num)
    if plus:
        treeCalculate(num+numbers[count], plus - 1, minos, multi, div, count)
    if minos:
        treeCalculate(num-numbers[count], plus, minos - 1, multi, div, count)
    if multi:
        treeCalculate(num*numbers[count], plus, minos, multi - 1, div, count)
    if div:
        treeCalculate(int(num/numbers[count]), plus, minos, multi, div-1, count)



for t in range(1, int(input()) + 1):
    length = int(input())
    PMMD_data = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    count = 0
    result_list = []
    treeCalculate(numbers[0], PMMD_data[0], PMMD_data[1], PMMD_data[2], PMMD_data[3], count)
    print('#{} {}'.format(t, max(result_list)-min(result_list)))


