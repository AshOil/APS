p = ")()()()("
from collections import deque

def is_balanced(string):
    return string.count("(") == string.count(")")

def is_corrected(string):
    Q = deque()
    for i in range(len(string)):
        if string[i] == "(":
            Q.append(string[i])
        else:
            if Q:
                Q.pop()
            else:
                return False
    if Q:
        return False
    return True

def v_cycle(v):
    result = ""
    if not v:
        return result
    for i in range(1, len(v) // 2 + 1):
        u2 = v[:i * 2]
        v2 = v[i * 2:]
        if is_balanced(u2):
            if is_corrected(u2):
                result += u2
                result += v_cycle(v2)
                return result
            else:
                result += "("
                result += v_cycle(v2)
                result += ")"
                u2 = u2[1:len(u2)-1]
                for j in u2:
                    if j == "(":
                        result += ")"
                    else:
                        result += "("
                return result
result = ""
print(v_cycle(p))