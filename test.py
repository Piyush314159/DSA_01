def mergeSort(arr, l, r):
    if l >= r:
        return

    mid = (l+r) // 2
    mergeSort(arr, l, mid)
    mergeSort(arr, mid+1, r)

    left = arr[l: mid+1]
    right = arr[mid+1: r+1]

    i = 0
    j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr

print(mergeSort([5,3,8,2,1,6,7],0,6))