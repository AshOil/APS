from itertools import permutations

def primeSearch(num):
    a = set([i for i in range(3, num, 2)])
    for i in range(3, num+1, 2):
        if i in a:
            a -= set([i for i in range(i*2, num+1, i)])
    return a

def solution(numbers):
    numbers = list(numbers) # 하나씩 분리
    all_list = []
    for i in range(1, len(numbers) + 1):
        all_list += list(map(list, permutations(numbers, i)))
    all_number = []
    for number in all_list:
        all_number.append(int(''.join(number)))
    prime_list = list(primeSearch(max(all_number)+1))
    prime_list.append(2)
    result = 0
    all_number = list(set(all_number))
    for number in all_number:
        if number in prime_list:
            result += 1
    return result


