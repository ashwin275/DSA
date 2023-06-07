

def BubbleSort(arr):
    for i in range(len(arr)):
        flag = 0
        for j in range(len(arr)-1-i):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
                flag = 1


        if flag == 0:
            break


    return arr


arr = [14,5,78,69,3,7,9,52,899]

print(BubbleSort(arr))