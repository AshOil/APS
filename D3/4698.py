## 시간 줄일 방안 ##


import sys
sys.stdin = open('input_data/4698.txt',"r")

T = int(input())

for t in range(1,T+1):
    favorite, start , end = list(map(int, input() .split()))
    prime_num = []
    
    for number in range(start, end):
        if favorite in str(number):
            for num in range(2,number):
                if number%num == 0:
                    break
                prime_num.append(number)
    my_prime = list(set(prime_num))
    print(my_prime)

        