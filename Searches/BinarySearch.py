# Binary search is an efficient algorithm for finding a specific value in a sorted list of elements

def BinarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [2, 3, 4, 5, 6, 7, 8, 9]
target = 6
search = BinarySearch(arr, target)

if search != -1:
    print(f'{target} found at {search+1}th position')
else:
    print(f'{target} is not in the arr')
