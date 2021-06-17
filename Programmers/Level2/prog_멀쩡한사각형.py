def solution(w,h):
    multi = w*h
    add = w+h
    while w != h:
        if w > h:
            w -= h
        else:
            h -= w
    return multi - (add - w)