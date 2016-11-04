import sys;

n = int(input("Enter your number: "))


def Interesting(n):
    checksum = 0
    initialN = n
    i = 0

    # Calculate Checksum
    while n > 0:
        checksum += n % 10
        n = int(n / 10)
    print("Checksum: ", checksum)

    # Decide if interesting number
    while i <= checksum:
        if (checksum ** i) == initialN:
            print("Interesting number!")
            print("%d = %d ^ %d" % (initialN, checksum, i))
            # print(initialN)
            return i
        else:
            i += 1
    print("Not an interesting number!")


Interesting(n)

# Calculate some interesting number (dont forget to comment some print-statements in the function)
# k = 0
# while k <= 1000:
#    Interesting(k)
#   k += 1