#Binary search using pointer approach
def binarysearch( arr, k):
    l = 0
    h = len(arr)- 1
    mid = 0
    while l <= h:
        mid=(l+h)//2
        if k > arr[mid]:
            l = mid + 1
        elif k<arr[mid]:
            h = mid - 1
        else:
            return mid

    return -1
arr = [ 2, 3, 4, 10, 40,50,60,90]
k = 60
result = binarysearch(arr,k)

if result != -1:
    print(result)
else:
    print("Element is not present in array")