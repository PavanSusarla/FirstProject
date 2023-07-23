def findTriplets(arr, n):
    found = False
    arr.sort()
    for i in range(0, n - 1):
        l = i + 1
        r = n - 1
        x = arr[i]
        while (l < r):
            if (x + arr[l] + arr[r] == 0):
                print(x, arr[l], arr[r])
                l += 1
                r -= 1
                found = True
                return 1
            elif (x + arr[l] + arr[r] < 0):
                l += 1
            else:
                r -= 1
    if (found == False):
        print("Not found")


arr = [0, -1, 2, -3, 1]
n = len(arr)
findTriplets(arr, n)
