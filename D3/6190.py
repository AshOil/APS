import sys
sys.stdin = open('input_data/6190.txt',"r")

T = int(input())

for t in range(1,T+1):
    length = int(input())
    numbers = list(map(int, input().split()))
    duo_list = []
    for i in numbers:
        for j in numbers:
            if i != j:
                if not i*j in duo_list:
                    duo_list.append(i*j)
    result_list = []
    for multi in list(map(str, duo_list)):
        standard = int(multi[0])
        for i in range(1,len(multi)):
            if int(multi[i]) < standard:
                break
        else:
            result_list.append(int(multi))
    print('#{} {}'.format(t, max(result_list)))


