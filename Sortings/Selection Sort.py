def SelectionSort(arr):

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


arr = [89, 6, 65, 4, 3, 8, 7, 32, 45, 6, 8, 9, 12, 35, 78]

SelectionSort(arr)
print(arr)