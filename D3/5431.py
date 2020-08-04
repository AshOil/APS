import sys
sys.stdin = open('input_data/5431.txt',"r")

T = int(input())

for t in range(1,T+1):
    total , count = list(map(int,input().split()))
    numbers = list(map(int,input().split()))
    num_list = []
    for i in range(1,total+1):
        num_list.append(i)
        for num in numbers:
            if num in num_list:
                num_list.remove(num)
    result = ' '.join(map(str, num_list))
    print('#{} {}'.format(t, result))


