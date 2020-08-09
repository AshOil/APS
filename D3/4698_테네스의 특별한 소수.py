import sys
sys.stdin = open('input_data/4698.txt',"r")

def PrimeSearch(num):
    a = set([i for i in range(3, num, 2)])
    for i in range(3, num+1, 2):
        if i in a:
            a -= set([i for i in range(i*2, num+1, i)])
    a.add(2)
    return a

T = int(input())
myprime = PrimeSearch(1000000)
print(myprime)
for t in range(1,T+1):
    count = 0
    favorite, start , end = list(map(int, input() .split()))
    for prime in myprime:
        if end>= prime >= start:
            if str(favorite) in str(prime):
                count += 1
    print('#{} {}'.format(t,count))

