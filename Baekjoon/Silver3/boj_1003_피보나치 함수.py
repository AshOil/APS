import sys
sys.stdin = open('input_data/1003.txt')


def Fibo(x):
    global memo
    if x >=2 and len(memo) <=2:
        memo.append(Fibo(x-1)+Fibo(x-2))
    if x == 0:
        global count_0
        count_0 +=1
    elif x ==1:
        global count_1
        count_1 +=1
    return memo[x]



T= int(input())
for _ in range(T):
    memo = [0, 1]
    count_0 = count_1 = 0
    print(Fibo(int(input())))
    print(count_0, count_1)

