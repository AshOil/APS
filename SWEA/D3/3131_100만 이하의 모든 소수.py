def prime_number():
    prime = set([i for i in range(3, 1000000, 2)])
    for i in range(3, 1000000, 2):
        if i in prime:
            prime -= set([j for j in range(i*2, 1000000, i)])
    prime.add(2)
    return sorted(prime)
print(*prime_number())
