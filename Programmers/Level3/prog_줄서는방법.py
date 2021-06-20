def get_num_check(n):
    num_check = [1] + [0]*(n-1)
    for i in range(2, n+1):
        num_check[i-1] = num_check[i-2] * i
    print(num_check)
    return num_check

def solution(n, k):
    numbers = [i+1 for i in range(n)]
    num_check = get_num_check(n)
    answer = []
    check = 0
    check_max = n - 2
    while check < n:
        answer.append(numbers.pop((k-1) // num_check[check_max]))
        k -= (k//num_check[check_max]) * num_check[check_max]
        check_max -= 1
        check += 1

    return answer

print(solution(3, 5))