citations = [0, 0, 0, 0]



def solution(citations):
    length = len(citations)
    for h in range(length, 0, -1):
        check = 0
        for j in range(length):
            if length - j + check < h:
                break
            if citations[j] >= h:
                check += 1
            if check >= h:
                return h
    else:
        return 0

print(solution(citations))


