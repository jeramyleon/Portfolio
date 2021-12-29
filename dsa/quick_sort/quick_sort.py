arr = [3, -2, -1, 0, 2, 4, 1]

def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j from l upto r - 1:
        if arr[j] < pivot:
            i += 1 
            swap arr[i] and arr[j]
    swap arr[i + 1] and arr[j]
    return i + l

def qs(arr, l, r): # l and r will represent index places in a list
    if l >= r:
        return 
    p = partition(arr, l, r) # we are going to write this function 
    
    qs(arr, l, p - 1)
    qs(arr, p + 1, r)

  