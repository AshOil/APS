import sys
sys.stdin = open('input_data/1244.txt',"r")

# def SelectionSort(a):
#     for i in range(0, len(a)-1):
#         min = i
#         for j in range(i+1, len(a)):
#             if a[min]>a[j]:
#                 min = j              # 여기까지 최솟값을 찾는 과정
#         a[i] , a[min] = a[min], a[i]
#
# T = int(input())
# for t in range(1,T+1):
#     number, turn = list(map(int, input().split()))
#     num_list = list(map(int,[num for num in str(number)]))
#     length = len(num_list)
#     start = 0
#     for _ in range(turn):
#         for idx, num in enumerate(num_list[::-1]):
#             if num == max(num_list):
#                 num_list[start], num_list[length - idx -1] = num_list[length - idx -1], num_list[start]
#                 start += 1
#     print(num_list)

T = int(input())
for t in range(1,T+1):
    number, turn = list(map(int, input().split()))
    num_list = list(map(int,[num for num in str(number)]))
    length = len(num_list)
    can_list = []
    can_list.append(list(num_list))
    while turn:
        num_list = list(can_list)
        can_list.clear()
        for data in num_list:
            for i in range(length-1):
                for j in range(i+1, length):
                    data[i], data[j] = data[j], data[i]
                    if data not in can_list:
                        can_list.append(list(data))
                    data[i], data[j] = data[j], data[i]
        turn -= 1
    print('#{} {}'.format(t, ''.join(map(str, max(can_list)))))




