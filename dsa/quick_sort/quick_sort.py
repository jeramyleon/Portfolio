def quicksort(arr):
    elements = len(arr)
    current_position = 0
    if elements < 2:
        return arr

    for i in range(1, elements): 
         if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp 
    
    left = quicksort(arr[0:current_position]) 
    right = quicksort(arr[current_position+1:elements]) 
    arr = left + [arr[current_position]] + right 
    return arr

array = [4, 2, 7, 3, 1, 6]
print("Original Array: ", array)
print("Sorted Array: ", quicksort(array))

def quick_sort(arr):
    elements = len(arr)
    current_position = 0
    if elements < 2:
        return arr
    
    for i in range(1, elements):
        if arr[i] <= arr[0]:
            current_position += 1
            temp = arr[i]
            arr[i] = arr[current_position]
            arr[current_position] = temp
    
    temp = arr[0]
    arr[0] = arr[current_position]
    arr[current_position] = temp

    left = quicksort(arr[0:current_position])
    right = quicksort(arr[current_position+1:elements])
    arr = left + [arr[current_position]] + right
    return arr

array = [4, 5, 6, 1, 2, 3, 7, 8, 9, 13, 14, 15, 11, 12, 13]
print("Original Array: ", array)
print("Sorted Array: ", quicksort(array))



