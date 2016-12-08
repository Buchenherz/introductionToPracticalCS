arr = [7, 8, 5, 2, 4, 9, 3, 1]
arr1 = [29, 14, 99, 23, 65, 39, 9, 0]

n = len(arr)

# O(N^2)
# Speicher: 2N (2 Arrays)

def swapSort(arr, n):
    i = 0
    m = 0
    while i < n:
        for counter in range(0, n):
            if arr[i] > arr[counter]:
                m += 1

        cp = arr[i]
        arr[i] = arr[m]
        arr[m] = cp

        if i is m:
            i += 1
        m = 0
    return arr

print("Swapsorted array:", swapSort(arr, n))