#Sort an array of 0s, 1s and 2s
# also the same as the famous “Dutch National Flag problem”
#This problem can be solved using the three Pointer Approach
def sort(arr, n):
    l = 0
    h = n - 1
    mid = 0
    while mid <= h:
        if arr[mid] == 0:
            arr[l], arr[mid] = arr[mid], arr[l]
            l = l + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid + 1
        else:
            arr[mid], arr[h] = arr[h], arr[mid]
            h = h - 1
    return arr
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1,1,1,1,2,0,0,0,2]
arr_size = len(arr)
arr = sort(arr, arr_size)
print(arr)
