arr = [69, 10, 30, 2, 16, 8, 31, 22, 30, 2, 5]
N = len(arr)

def getMin(s,e):
    if s == e:
        return s
    else:
        ret = getMin(s, e-1)
        return ret if arr[ret] < arr[e] else e

def selectionSort(s,e):
    if s == e: return
    idx = getMin(s, e)
    arr[s], arr[idx] = arr[idx], arr[s]
    selectionSort(s+1, e)


getMin(0,N-1)
selectionSort(0, N-1)
print(arr)