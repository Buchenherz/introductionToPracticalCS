
n = int(input("Enter your number: "))


def Interesting(n):
    checksum = 0
    initialN = n
    i = 0

    # Calculate Checksum
    while n > 0:
        checksum += n % 10
        # would previously return a float value
        n = int(n / 10)
    print("Checksum:", checksum)

    # Decide if interesting number
    while i <= checksum:
        # Is checksum^i == to previous N?
        if (checksum ** i) == initialN:
            # print(initialN, "is an interesting number!")
            print("Interesting number!")
            print("%d = %d ^ %d" % (initialN, checksum, i))
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