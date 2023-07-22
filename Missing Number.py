#Missing number in array
#Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.
def getMissingNo(arr, n):#Function for missing number
    sums=sum(arr)
    res=(n*(n+1))//2-sums
    return res
array = [1, 2, 3, 5, 6]
N=len(array)+1
print(getMissingNo(array, N))