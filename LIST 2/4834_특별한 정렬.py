import sys
sys.stdin = open('input_data/4834.txt',"r")

def SelectionSort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min]>a[j]:
                min = j              # 여기까지 최솟값을 찾는 과정
        a[i] , a[min] = a[min], a[i]

T = int(input())

for t in range(1, T+1):
    length = int(input())
    numbers = list(map(int, input(). split()))
    SelectionSort(numbers)
    result_list = []
    for i in range(5):
        result_list.append(numbers[-(i+1)])
        result_list.append(numbers[i])
    print_result = ' '.join(map(str,result_list))

    print('#{} {}'.format(t, print_result))

