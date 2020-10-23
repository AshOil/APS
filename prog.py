from itertools import product

my_num = [1, 2, 4]

number = 10

for i in range(1, 10000):
    if 3**(i-1) < number <= 3**i:
        break
print(i)
number = number - 3**(i-1)
check_list = []
for j in product([1, 2, 4], repeat=i):
    check_list.append(i)
print(check_list)