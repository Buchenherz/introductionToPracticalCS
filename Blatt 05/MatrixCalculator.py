import random

# creates matrix with m columns and n rows and fills it
# with random ints between 0 and 100

# For testing only, uncomment all m, n's and scalar
# scalar = m = n = x = y = 200

def matrix(m,n):

    # [[0 for x in range(cols_count)] for x in range(rows_count)]
    Matrix = [[random.randint(0,5) for x in range(m)] for y in range(n)]

    # nice print of the matrix
    for row in Matrix:
        print(row)

    return Matrix

def scalar_multiplication():

    print("Create Matrix:")
    m = int(input("m = "))
    n = int(input("n = "))
    Matrix = matrix(m, n)

    scalar = int(input("Enter scalar: "))

    # every item times 3
    for j in range(0, n):
        for i in range(0, m):
            Matrix[i][j] *= scalar
    for row in Matrix:
        print(row)

def matrix_addition():

    print("Create first Matrix:")
    m = int(input("m = "))
    n = int(input("n = "))
    a = matrix(m, n)

    print()

    print("Create second Matrix:")
    x = int(input("m = "))
    y = int(input("n = "))
    b = matrix(x, y)

    if m is x and n is y:
        Matrix = [[0 for x in range(m)] for y in range(n)]
        for j in range(0, m):
            for i in range(0, n):
                Matrix[i][j] = a[i][j] + b[i][j]
    else:
        print("Please choose two Matrices that have equal m and n")

    print()

    print("Matrix 1 + Matrix 2 =")
    for row in Matrix:
                print(row)

def matrix_multiplication():

        print("Create first Matrix:")
        m = int(input("m = "))
        n = int(input("n = "))
        a = matrix(m, n)

        print()

        print("Create second Matrix:")
        x = int(input("m = "))
        y = int(input("n = "))
        b = matrix(x, y)

        if n is x:
            Matrix = [[0 for x in range(m)] for y in range(x)]
            for j in range(0, m):
                for i in range(0, n):
                    for k in range(0,n):
                        Matrix[i][j] += a[i][k] * b[k][j]
        else:
            print("Huston, we have a problem. n of Matrix 1 needs to be equal with m of Matrix 2")

        print()

        print("Matrix 1 * Matrix 2 =")
        for row in Matrix:
            print(row)

def matrix_transposistion():

    print("Create Matrix:")
    m = int(input("m = "))
    n = int(input("n = "))
    a = matrix(m, n)

    # create empty matrix with n rows and m columns
    Matrix = [[0 for x in range(n)] for y in range(m)]
    for j in range(0, m):
        for i in range(0, n):
            Matrix[j][i] = a[i][j]

    print("Matrix 1 transposed =")
    for row in Matrix:
        print(row)

def matrix_calculator():
    while True:

        print("/*=======================================\n")
        print("=              Calculator:              =\n")
        print("+          1 - Matrix Addition          +\n")
        print("*        2 - Matrix Multiplication      *\n")
        print("*        3 - Scalar Multiplication      *\n")
        print("q               0 - Quit                q\n")
        print("=======================================*/\n")

        option = int(input("Choose an option: "))

        if option is 0:
            return SystemExit
        elif option is 1:
            matrix_addition()
        elif option is 2:
            matrix_multiplication()
        elif option is 3:
            scalar_multiplication()

matrix_calculator()
#matrix_transposistion()
#matrix_multiplication()
#matrix_addition()
#scalar_multiplication()