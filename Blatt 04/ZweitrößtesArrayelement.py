# import function from file
from ArrayInitialisierung import initArray

# variable declaration
z = int(input("Enter number Z (rng from 0 to Z): ")) # Whole number - will be used from 0 to Z
n = int(input("Enter array length N: ")) # Array length - number of array items

# pass initArray function to a
a = initArray(z, n)

# set max to first item of array
max = a[0]
# set prevMax to 0
prevMax = 0

# iterate over array (start with second item)
for i in range(1,n):
    # is max smaller than next item?
    if max < a[i]:
        # if, then set prevMax to max
        prevMax = max
        # and max to the greater value (next item)
        max = a[i]
    # when max is already reached and prevMax is smaller
    # than next array number
    if prevMax < a[i] and max > a[i]:
        # set prevMax to next array number
        prevMax = a[i]

print("Array:", a)
print("Max value:", max)
print("Second biggest value:", prevMax)