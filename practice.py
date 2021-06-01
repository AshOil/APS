def bubbleSort(x):
    length = len(x) - 1
    for i in range(length):
        for j in range(length - i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
                print(x)
    return x


def selectionSort(x):
    length = len(x)
    for i in range(length-1):
        min_idx =  i
        for j in range(i+1, length):
            if x[min_idx] > x[j]:
                min_idx = j
        x[i], x[min_idx] = x[min_idx], x[i]
        print(x)
    return x

def insertSort(x):
    for i in range(1, len(x)):
        j = i - 1
        key = x[i]
        while x[j] > key and j >= 0:
            x[j+1] = x[j]
            j = j - 1
            x[j+1] = key
        print(x)
    return x

def quickSort(x):
    if len(x) <= 1:
        return x

    pivot = x[len(x) // 2]
    less = []
    more = []
    equal = []
    for a in x:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    print(f"작은 + {less}")
    print(f"기준 + {equal}")
    print(f"큰 + {more}")
    print("--------------")
    return quickSort(less) + equal + quickSort(more)

x = [5, 7, 4, 2, 6, 8, 1, 3]

# print(bubbleSort(x))
# print(selectionSort(x))
# print(insertSort(x))
print(quickSort(x))