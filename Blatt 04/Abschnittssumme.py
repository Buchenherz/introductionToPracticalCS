from ArrayInitialisierung import initArray

n = z = 10000#int(input("Enter number Z (rng from 0 to Z): ")) # Whole number - will be used from 0 to Z
#n = int(input("Enter array length N: ")) # Array length - number of array items

a = initArray(z, n)
print(a)

def linear(a, n):
    max = 0
    sum = 0
    for i in range(0, n):
        sum += a[i]
    if(sum > 0):
        if (sum > max):
            max = sum
        else:
            sum = 0
    print(max)
    return max

# linear(a)

def squared(a, n):
    max = 0
    for i in range(0, n):
        sum = 0
        for j in range(i, n):
            sum += a[j]
            if(sum > max):
                max = sum
    print(max)
    return max

def cubed(a, n):
    max = 0
    for i in range(0, n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j+1):
                sum += a[k]
            if(sum > max):
                max = sum
    print(max)
    return max

#linear(a,n)
#squared(a,n)
cubed(a,n)
