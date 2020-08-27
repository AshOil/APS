
def PrimeSearch(num):
    a = set([i for i in range(3, num, 2)])
    for i in range(3, num+1, 2):
        if i in a:
            a -= set([i for i in range(i*2, num+1, i)])
    return a

print(PrimeSearch(1000000))
