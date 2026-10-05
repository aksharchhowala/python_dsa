def bubble_sort(arr):
    for i in range(len(arr)-1):
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


num_list = [2,5,3,9,8,4,7,26,6,3,5,1,8,15,0]
print(bubble_sort(num_list))