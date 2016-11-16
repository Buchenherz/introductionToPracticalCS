import random

# Variable initialisation
#z = int(input("Enter number Z (rng from 0 to Z): ")) # Whole number - will be used from 0 to Z
#n = int(input("Enter array length N: ")) # Array length - number of array items

def initArray(z, n):

    # Create array with size n
    a = [0] * n

    # Go through every element in the array...
    for i in range(0,n):
        #...and set a random number between 0 and z
        a[i] = random.randint(0,z)
    # So we see something
    # print(a)
    # Return the array
    return a

# Function call
# initArray(z, n)