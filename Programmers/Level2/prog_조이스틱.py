## 요거하면 마지막ㄲ ㅓ하나 틀림


def solution(name):
    result = len(name) - 1
    for char in name:
        count = ord(char) - ord('A')
        if count > 13:
            result += 26 - count
        else:
            result += count
    left_check = 0
    right_check = 0
    for i in range(1, len(name)):
        if name[i] == 'A':
            left_check += 1
        else:
            break
    for i in range(len(name) - 1, 0, -1):
        if name[i] == 'A':
            right_check += 1
        else:
            break
    result -= max(left_check, right_check)

    return result