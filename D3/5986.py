import sys
sys.stdin = open('input_data/5986.txt',"r")

def PrimeSearch(num):
    a = set([i for i in range(3, num, 2)])
    for i in range(3, num+1, 2):
        if i in a:
            a -= set([i for i in range(i*2, num+1, i)])
    a.add(2)
    return a

T = int(input())
for t in range(1, T+1):
    number = int(input())
    # 소수 갯수 구하기
    prime_list = PrimeSearch(number)
    print(prime_list)
    # 3개로 이루어진 집합 구하기
    sumlist = []
    for i in prime_list:
        for j in prime_list:
            for k in prime_list:
                sumlist.append(sorted([i,j,k]))
    # 중복 제거하기
    new_sumlist = []
    for sums in sumlist:
        if not sums in new_sumlist:
            new_sumlist.append(sums)

    count = 0
    for sums in new_sumlist:
        if sum(sums) == number:
            count += 1
    print('#{} {}'.format(t, count))





