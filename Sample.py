def selectionSort(arr):
    for i in range(len(arr) - 1):

        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def bubbleSort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            break

    return arr


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quickSort(left) + mid + quickSort(right)


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = [3, 2, 4, 5, 67, 1, 8, 1]
print(selectionSort(arr))
print(bubbleSort(arr))
print(insertionSort(arr))
print(quickSort(arr))
print(mergeSort(arr))

list = [3, -2, 5, 6, 7, -5, -4, -2]
for i in range(len(list)):
    if i % 2 == 0 and not list[i] > 0:
        for j in range(i + 1, len(list)):
            if list[j] > 0:
                list[j], list[i] = list[i], list[j]
    elif i % 2 == 1 and not list[i] < 0:
        for k in range(i + 1, len(list)):
            if list[k] < 0:
                list[k], list[i] = list[i], list[k]

print(list)
