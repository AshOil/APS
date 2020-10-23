def primeSearch(num):
    a = set([i for i in range(3, num, 2)])
    for i in range(3, num+1, 2):
        if i in a:
            a -= set([i for i in range(i*2, num+1, i)])
    return a

def powerSet(num_list):
    n = len(num_list)
    total_list = []
    for i in range(1<<n):
        in_list = []
        for j in range(n):
            if i & (1<<j):
                in_list.append(num_list[j])
        total_list.append(in_list)
    return total_list

numbers = '011'
num_list = list(numbers)
check = []
combinations = powerSet(num_list)
print(combinations)
for number in combinations:
    if number:
        check.append(int(''.join(number)))
print(check)
prime_list = list(primeSearch(10**(len(num_list))))
result = 0
for i in check:
    if i in prime_list:
        result +=1
