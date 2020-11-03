
arr = [69, 10, 30, 2, 16, 8, 31, 22]
# 병합 작업

tmp = [0] * len(arr)  # 임시공간
def mergeSort(lo, hi):
    if lo == hi : return
    mid = (lo+hi) >> 1  # 나누기 2(비트연산자로 1칸씩 이동하면 2로 노나짐)
    mergeSort(lo, mid)
    mergeSort(mid+1, hi)
    i, j, k = lo, mid+1, lo
    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i, k = i + 1, k + 1
        else:
            tmp[k] = arr[j]
            j, k = j + 1, k + 1
    while i <= mid:
        tmp[k] = arr[i]
        i, k = i + 1, k + 1
    while j <= hi:
        tmp[k] = arr[j]
        j, k = j + 1, k + 1

    for i in range(lo, hi + 1):
        arr[i] = tmp[i]

mergeSort(0, len(arr) - 1)
print(arr)

def quickSort(lo, hi):
    if lo >= hi:return
    # 파티션 p = partition(lo, hi)
    i, j = lo, hi

    while i < j:
        while arr[lo] > arr[i]:
            i += 1
        while arr[lo] < arr[j]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[j] = arr[j], arr[lo]

    quickSort(lo, j-1)
    quickSort(j+1, hi)

quickSort(0, len(arr)-1)
print(arr)