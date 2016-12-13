import random

# Variable initialisation
#z = int(input("Enter number Z (rng from 0 to Z): ")) # Whole number - will be used from 0 to Z
#n = int(input("Enter array length N: ")) # Array length - number of array items

z = 10
n = 100000000

def initArray(z, n):
    arr = [0] * n
    for i in range(0,n):
        arr[i] = random.randint(0,z)
    print("Unsorted array:", arr)
    return arr

arr = initArray(z, n)

def shakerSort(arr, n):
    b = False
    k = 1
    while k < n and not b:
        b = True

        # Go through first to last
        for i in range(0, n - k):

            if arr[i] > arr[i + 1]:
                t = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = t
                switch = 1
                b = False

            elif arr[n-k] < arr[n-k-i]:
                t = arr[n-k]
                arr[n-k] = arr[n-k-i]
                arr[n-k-i] = t
                switch = 0
                b = False

        k += 1
    return arr;

#print("Shakersorted array:", shakerSort(arr, n))

import random


def initArray(z, n):
    arr = [0] * n
    for i in range(0,n):
        arr[i] = random.randint(0,z)
    print("Unsorted array:", arr)
    return arr

arr = initArray(z, n)

def countingSort(arr, n):

    counter = [0] * (n + 1)
    for i in arr:
        counter[i] += 1

    index = 0

    for i in range(len(counter)):
        while 0 < counter[i]:
            arr[index] = i
            index += 1
            counter[i] -= 1
    return arr

print("Countingsorted array:", countingSort(arr, n))