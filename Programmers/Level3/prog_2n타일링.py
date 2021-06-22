def solution(n):
    check = [0,1,2] + [0] * (n-2)
    for i in range(3, n+1):
        check[i] = (check[i-1] + check[i-2])%1000000007
    return check[n]