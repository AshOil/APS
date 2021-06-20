check = [100] * 12
result = 0
def solution(n):
    def queen(now):
        global result
        if now == n:
            result += 1
        else:
            if now == 0:
                for i in range(n):
                    check[now] = i
                    queen(now+1)
                    check[now] = 100
            else:
                for i in range(n):
                    if i not in check:
                        for j in range(1, now+1):
                            if i == check[now - j] + j or i == check[now - j] - j:
                                break
                        else:
                            check[now] = i
                            queen(now+1)
                            check[now] = 100
    queen(0)
    return result

