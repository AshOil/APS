import sys; sys.stdin = open('input_data/10965.txt')

def prime_check(num):
    prime = set([i for i in range(3, num+1, 2)])
    for i in range(3, num+1, 2):
        if i in prime:
            prime -= set([j for j in range(i*2, num+1, i)])
    prime.add(2)
    return prime

print(prime_check(1))

# for t in range(1, int(input()) + 1):
#     check = []
#     number = int(input())
#     prime = prime_check(number)
#     if number in prime:
#         print('#{} {}'.format(t, number))
#         continue
#     for i in range(1, number+1):
#         if ((number*i)**0.5)%1:
#             continue
#         else:
#             print('#{} {}'.format(t, i))
#             break

