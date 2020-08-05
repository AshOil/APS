import sys
sys.stdin = open('input_data/5986.txt',"r")

prime_list = [2]
for number in range(3,1000):
    prime_num = True
    for num in range(2,number):
        if not number%num:
            prime_num = False
            break
    if prime_num:
        prime_list.append(number)

T = int(input())
for t in range(1, T+1):
    number = int(input())
    my_prime = []
    for num in prime_list:
        if num < number:
            my_prime.append(num)
    length = len(my_prime)
    sumlist = []
    for i in my_prime:
        for j in my_prime:
            for k in my_prime:
                sumlist.append(sorted([i,j,k]))
    new_sumlist = []
    for sums in sumlist:
        if not sums in new_sumlist:
            new_sumlist.append(sums)

    count = 0
    for sums in new_sumlist:
        if sum(sums) == number:
            count += 1
    print('#{} {}'.format(t, count))





