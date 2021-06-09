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

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    # 이때 slice를 사용하는 건 코드상 깔끔해지지만
    # list의 복사가 일어나기 때문에 메모리 효율은 떨어질 수 있다.
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    # 줄세워 놓은거 0번부터 시작
    while l < len(low_arr) and h < len(high_arr):
        # 시작부터 하나씩 비교해서 더 작은거 merge_arr에 넣고, 한칸 앞으로
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    # 하나가 끝났으면, 나머지 그냥 넣어버리기
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    print(merged_arr)
    return merged_arr


def merge_sort_upgrade(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]
        print(x)

    return sort(0, len(arr))

def heap_sort(arr):
    # 최대 힙 만들기
    for i in range(1, len(arr)):
        c = i
        while c:
            p = (c-1) // 2
            if arr[p] < arr[c]:
                arr[p], arr[c] = arr[c], arr[p]
            c = p

    # 힙 만들기
    for j in range(len(arr)-1, -1, -1):
        arr[0], arr[j] = arr[j], arr[0]
        p = 0
        c = 1
        while c < j:
            c = 2*p + 1
            if c < j - 1 and arr[c] < arr[c+1]:
                c += 1
            if c < j and arr[p] < arr[c]:
                arr[p], arr[c] = arr[c], arr[p]
            p = c
            print(arr)



def radix_sort(num):
    # 최대 digit을 알아보기 위해 가장 큰 수를 찾는다
    max1 = max(num)
    exp = 1
    while max1 / exp > 0:
        count_sort(num, exp)
        exp *= 10

def count_sort(A, k):
    B = [0] * len(A)
    C = [0] * (10)  # 1의 자리, 10의 자리수만 비교하기 때문에 범위는 0~9이다

    for i in range(0, len(A)):  # 각 element가 몇개있는지 C에 저장한다
        index = (A[i] // k)
        C[(index) % 10] += 1

    for i in range(1, 10):  # C를 누적값으로 바꾼다, 0~9까지 밖에 없다
        C[i] += C[i - 1]

    i = len(A) - 1
    while i >= 0:  # C 를 indexing해서 정렬된 리스트를 찾는다
        index = (A[i] // k)
        B[C[(index) % 10] - 1] = A[i]
        C[(index) % 10] -= 1
        i -= 1

    # 기존 리스트에 복사를 한다
    for i in range(len(A)):
        A[i] = B[i]


x = [5, 7, 4, 2, 6, 8, 1, 3]
print(x)
radix_sort(x)
print(x)

