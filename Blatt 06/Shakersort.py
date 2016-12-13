import random

# Variable initialisation
z = int(input("Enter number Z (rng from 0 to Z): ")) # Whole number - will be used from 0 to Z
n = int(input("Enter array length N: ")) # Array length - number of array items

# O(N^2)
# Speicher: N

def initArray(z, n):
    arr = [0] * n
    for i in range(0,n):
        arr[i] = random.randint(0,z)
    print("Unsorted array:", arr)
    return arr

arr = initArray(z, n)

def shakerSort(arr):
   while True:
       swapped = False
       # From bottom to top
       for i in range(0, len(arr)-2):
           if arr[i] > arr[i+1]:
               tmp = arr[i+1]
               arr[i+1] = arr[i]
               arr[i] = tmp
               swapped = True
       if not swapped:
           break
       swapped = False
       # From top to bottom
       for i in range(len(arr)-2, 0, -1):
           if arr[i] > arr[i+1]:
               tmp = arr[i + 1]
               arr[i + 1] = arr[i]
               arr[i] = tmp
               swapped = True
   return arr

print("Shakersorted array:", shakerSort(arr))
