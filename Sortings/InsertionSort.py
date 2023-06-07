def InsertionSort(arr):

    for i in range(1,len(arr)):
        j = i-1
        key = arr[i]

        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1

        arr[j+1] =  key

    return arr


arr = [4,7,8,9,6,3,78,2,69,90,245]

print(InsertionSort(arr))