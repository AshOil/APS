def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

print(get_natural_number())

g = get_natural_number()
for _ in range(100):
    print(next(g))
g = get_natural_number()
for _ in range(100):
    print(next(g))
