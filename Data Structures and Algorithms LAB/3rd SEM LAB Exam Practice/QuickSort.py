def partition(arr, l, r):
    i = l
    j = r - 1
    pivot = arr[r]
    while i < j:
        if i < r and arr[i] < pivot:
            i += 1
        if j > l and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[r] = arr[r], arr[i]
    return i


def QuickSort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        QuickSort(arr, l, p - 1)
        QuickSort(arr, p + 1, r)


arrList = list(map(int, input().split(", ")))
QuickSort(arrList, 0, len(arrList)-1)
print(arrList)
