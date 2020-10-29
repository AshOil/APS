import sys
sys.stdin = open('input_data/1244.txt',"r")

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




