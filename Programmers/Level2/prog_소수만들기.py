nums = [1,2,7,6,4]

from itertools import combinations

def prime_search(number):
    prime = set([i for i in range(3, number+1, 2)])
    for i in range(3, number+1, 2):
        if i in prime:
            prime -= set([j for j in range(i**2, number+1, i)])
    prime.add(2)
    return prime

def solution(nums):
    prime_list = prime_search(3000)
    can_list = list(map(list, combinations(nums, 3)))
    result = 0
    for can in can_list:
        if sum(can) in prime_list:
            result += 1
    return result

