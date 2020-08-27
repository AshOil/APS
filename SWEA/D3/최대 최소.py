arr = [3,6,7,1,5,4]

for idx in range(0, len(arr) - 1):
    for i in range(idx +1, len(arr)):
        if arr[idx] > arr[i] : idx = i
    arr[j]