## 맞는거 같은데 왜 틀리다그러지 ㅠㅠ

import sys
sys.stdin = open('input_data/1934.txt', "r")

T = int(input())
for _ in range(T):
    A, B = list(map(int, input().split()))
    result = B
    # 작은 수를 A로 하기 위해 swap
    if A > B:
        A, B = B, A
    A_baby = {}
    B_baby = {}

    # A 랑 B 인수분해 해서 dict.에 넣기
    while A != 1:  # 인수로 계속 나눠 1이 될때까지 진행
        for i in range(2,A+1):
            if not A%i:  # 나누어 떨어지면
                if i in A_baby:  # dict에 이미 있는 수면 1 더하고
                    A_baby[i] += 1
                else :          # 없는 수면 새로 key 하나 만들기
                    A_baby[i] = 1
                A = int(A/i)    # 인수로 나누기
                break    # 인수가 나오면 for문 밖으로 나오기
    while B != 1:
        for i in range(2,B+1):
            if not B%i:
                if i in B_baby:
                    B_baby[i] += 1
                else :
                    B_baby[i] = 1
                B = int(B/i)
                break

    # A 돌려가면서 B에 부족한거 채워주기
    for key , value in A_baby.items():
        if key in B_baby:
            if value > B_baby[key]:
                result *= key**(value-B_baby[key])
        else:
            result *= key**value
    print(result)

