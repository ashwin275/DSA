def QuickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = []
    right = []
    mid = []

    for x in arr:
        if x < pivot:

            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            mid.append(x)

    return QuickSort(left) + mid + QuickSort(right)


arr = [3, 2, 2, 4, 2, 5, 7, 1, 9, 34]

print(QuickSort(arr))


def QuickSort2(arr):
    if len(arr) < 1:
        return arr
    pivot = arr[len(arr) // 2]
    right = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    left = [x for x in arr if x > pivot]

    return QuickSort2(right) + mid + QuickSort2(left)


arr2 = [3, 4, 2,2, 3, 6, 8, 9]
print(QuickSort2(arr2))

