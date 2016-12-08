import random

# Variable initialisation
z = int(input("Enter number Z (rng from 0 to Z): ")) # Whole number - will be used from 0 to Z
n = int(input("Enter array length N: ")) # Array length - number of array items

# O(NlogN)
# Speicher: N

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

    for i in range(0, len(counter)):
        while 0 < counter[i]:
            arr[index] = i
            index += 1
            counter[i] -= 1
    return arr

print("Countingsorted array:", countingSort(arr, n))